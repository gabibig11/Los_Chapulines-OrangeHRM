import requests
import pytest
import jsonschema
from config import system_url
from src.assertions.location_assertions import assert_location_schema, assert_location_id_schema
from src.orangeHRM_api.api_requests import OrangeRequests
from src.orangeHRM_api.endpoints import Endpoints
@pytest.mark.smoke
def test_get_all_locations(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    actual_count = len(response.json()['data'])
    assert actual_count == 551, f'La cantidad de elementos que devolvio la consulta no es igual a 551 esperados'
    assert response.status_code == 200

def test_get_locations_invalid_token(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Authorization': f'{test_login}4'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 401
    assert response.json()['error'] == "invalid_token"
    assert response.json()['error_description'] == "The access token provided is invalid"

def test_get_location_token_empty():
    url = f'{system_url}{Endpoints.location.value}'
    headers = { }
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 401
def test_get_location_filter_name(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[name]=adonis.net'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    response_data = response.json()
    assert response.status_code == 200


def test_get_location_filter_city(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=West%Briannetown'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    response_data = response.json()
    assert response.status_code == 200


def test_get_location_filter_countryCode(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[countryCode]=AU'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    response_data = response.json()
    assert response.status_code == 200


def test_get_location_filter_id(test_login):
    url = f'{system_url}{Endpoints.location.value}/564'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_id_schema(response.json()) == True
    response_data = response.json()
    assert response.status_code == 200