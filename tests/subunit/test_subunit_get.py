import requests
import pytest
from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.assertions.subunit_assertions_get import (
    assert_subunit_auth_error,
    assert_subunit_schema,
    assert_subunit_list_schema,
    assert_subunit_not_found,
    assert_subunit_list_sorted,
    assert_subunit_invalid_request
)

from src.assertions.subunit_assertions_get import assert_subunit_auth_error

@pytest.mark.smoke
def test_get_subunit_valid_id(test_login):
    subunit_id = 1
    url = f'{system_url}{Endpoints.subunits.value}/{subunit_id}'
    headers = {'Authorization': f'Bearer {test_login}'}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data['data']['id'] == str(subunit_id)

    assert_subunit_schema(response.json())


def test_get_subunit_invalid_token():
    subunit_id = 1
    url = f'{system_url}{Endpoints.subunits.value}/{subunit_id}'
    headers = {'Authorization': 'Bearer invalid_token'}
    response = requests.get(url, headers=headers)

    assert response.status_code == 401
    assert_subunit_auth_error(response.json(), {
        "error": "invalid_token",
        "error_description": "The access token provided is invalid"
    })


def test_get_subunit_no_token():
    subunit_id = 1
    url = f'{system_url}{Endpoints.subunits.value}/{subunit_id}'
    response = requests.get(url)

    assert response.status_code == 401
    assert_subunit_auth_error(response.json(), {
        "error": "invalid_request",
        "error_description": "Malformed auth header"
    })


def test_get_subunit_not_found(test_login):
    subunit_id = 9999  # Assuming this ID does not exist
    url = f'{system_url}{Endpoints.subunits.value}/{subunit_id}'
    headers = {'Authorization': f'Bearer {test_login}'}
    response = requests.get(url, headers=headers)

    assert response.status_code == 404
    assert_subunit_not_found(response.json())


def test_get_subunits_list(test_login):
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Authorization': f'Bearer {test_login}'}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert_subunit_list_schema(response.json())


def test_get_subunits_with_name_filter(test_login):
    url = f'{system_url}{Endpoints.subunits.value}?fields[]=name'
    headers = {'Authorization': f'Bearer {test_login}'}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert 'data' in response.json()
    for subunit in response.json()['data']:
        assert 'name' in subunit


def test_get_subunits_with_cost_centre_id_filter(test_login):
    url = f'{system_url}{Endpoints.subunits.value}?fields[]=cost_centre_id'
    headers = {'Authorization': f'Bearer {test_login}'}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert 'data' in response.json()
    for subunit in response.json()['data']:
        assert 'cost_centre_id' in subunit


def test_get_subunits_sorted_asc(test_login):
    url = f'{system_url}{Endpoints.subunits.value}?sortingOrder=ASC'
    headers = {'Authorization': f'Bearer {test_login}'}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert_subunit_list_sorted(response.json(), "ASC")


def test_get_subunits_sorted_desc(test_login):
    url = f'{system_url}{Endpoints.subunits.value}?sortingOrder=DESC'
    headers = {'Authorization': f'Bearer {test_login}'}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert_subunit_list_sorted(response.json(), "DESC")


def test_get_subunits_invalid_request(test_login):
    url = f'{system_url}{Endpoints.subunits.value}?invalid_param=true'
    headers = {'Authorization': f'Bearer {test_login}'}
    response = requests.get(url, headers=headers)

    assert response.status_code == 400 or response.status_code == 200
    assert_subunit_invalid_request(response.json())

def assert_subunit_auth_error(response, expected_error):
    assert response["error"] == expected_error["error"]
    assert response["error_description"] == expected_error["error_description"]
