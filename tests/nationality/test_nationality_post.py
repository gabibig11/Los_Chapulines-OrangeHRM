import json
import pytest
from conftest import test_login, post_teardown
from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests
from src.assertions.nationality_assertions import assert_invalid_token, assert_json_structure, \
    assert_invalid_parameters, assert_data_keys, assert_nationality_post_schema, assert_nationality_post_schema_response


@pytest.mark.smoke
def test_post_nationality_success(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "name": "Catan"
    }
    assert assert_nationality_post_schema(payload) == True
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 201
    assert assert_nationality_post_schema_response(response.json()) == True
    #response_json = response.json()
    #assert_json_structure(response_json)
    #assert_data_keys([response_json['data']])
    post_teardown(url=url, headers=headers, response=response.json(),attribute_search="id", attribute_delete="data", array=True)
def test_post_nationality_invalid_token():
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer invalid_token'}
    payload = json.dumps({"name": "Catan"})
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
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

