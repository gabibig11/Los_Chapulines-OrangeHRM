import json
import pytest
from conftest import test_login, post_teardown
from config import system_url, expired_token, random_token
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests
from src.assertions.nationality_assertions import assert_invalid_token, assert_json_structure, \
    assert_invalid_parameters, assert_data_keys, assert_nationality_post_schema, \
    assert_nationality_post_schema_response, \
    assert_nationality_name_exceeds_max_length
from src.resources.functions.nationality import random_info


@pytest.mark.smoke
def test_post_nationality_success(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "name": "Catan"
    }
    assert assert_nationality_post_schema(payload) == True
    payload = {
        "name": "Catan"
    }
    assert assert_nationality_post_schema(payload) == True
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 201
    assert assert_nationality_post_schema_response(response.json()) == True
    post_teardown(url=url, headers=headers, response=response.json(), attribute_search="id", attribute_delete="data",
                  array=True)


def test_post_nationality_invalid_token():
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer invalid_token'}
    payload = json.dumps({"name": "Catan"})
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 401
    assert response.status_code == 401
    response_json = response.json()
    assert_invalid_token(response, response_json)


def test_post_nationality_missing_name(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = json.dumps({})
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert_invalid_parameters(response)
    response_json = response.json()
    assert_json_structure(response_json)


def test_post_nationality_empty_token():
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '}
    payload = json.dumps({"name": "Catan"})
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 401
    response_json = response.json()
    assert 'error' in response_json
    assert response_json['error'] == 'invalid_request'


def test_nationality_post_no_authorization():
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer valid_token'}
    response = OrangeRequests().post(url=url, headers=headers)
    assert response.status_code == 401


def test_existing_nationality_post(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {

        "name": "Catan"
    }
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 201
    post_teardown(url=url, headers=headers, response=response.json(), attribute_search="id", attribute_delete="data",
                  array=True)


def test_post_nationality_empty_name():
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = json.dumps({"name": ""})
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert_invalid_parameters(response)
    response_json = response.json()
    assert 'error' in response_json


def test_post_nationality_extra_field():
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = json.dumps({"name": "Catan", "extra_field": "value"})
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert_invalid_parameters(response)
    response_json = response.json()
    assert 'error' in response_json


@pytest.mark.xfail(reason="Server currently returns 500 instead of 400 for name length exceed")
def test_post_nationality_name_exceeds_max_length(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {"Name": f'{random_info(101)}'}
    response = OrangeRequests().post(url=url, headers=headers, data=json.dumps(payload))
    assert response.status_code == 400

