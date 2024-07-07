import json
import pytest
from conftest import test_login, post_teardown
from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests
from src.assertions.nationality_assertions import AssertionNationality

@pytest.mark.smoke
def test_post_nationality_success(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = json.dumps({"name": "Catan"})
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    AssertionNationality.assert_status_code(response, 201)
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.json())
    response_json = response.json()
    AssertionNationality.assert_json_structure(response_json)
    AssertionNationality.assert_data_keys([response_json['data']])
    post_teardown(url=url, headers=headers, response=response, attribute="data")
def test_post_nationality_invalid_token():
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer invalid_token'}
    payload = json.dumps({"name": "Catan"})
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    AssertionNationality.assert_status_code(response, 401)
    response_json = response.json()
    AssertionNationality.assert_invalid_token(response, response_json)

def test_post_nationality_missing_name(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = json.dumps({})
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    AssertionNationality.assert_invalid_parameters(response)
    response_json = response.json()
    AssertionNationality.assert_json_structure(response_json)

