import requests
from config import system_url, client_id, client_secret, grant_type
import jsonschema
import pytest
from src.orangeHRM_api.endpoints import Endpoints
from src.assertions.login_assertions import assert_login_success, assert_login_failed, assert_login_schema, assert_login_blocked


def test_login_success():
    url = f'{system_url}{Endpoints.login.value}'
    payload = {'client_id': f'{client_id}', 'client_secret': f'{client_secret}',
               'grant_type': f'{grant_type}'}
    response = requests.post(url, data=payload)
    assert response.status_code == 200
    assert_login_success(response.json())


def test_login_json():
    url = f'{system_url}{Endpoints.login.value}'
    payload = {'client_id': f'{client_id}', 'client_secret': f'{client_secret}',
               'grant_type': f'{grant_type}'}
    response = requests.post(url, data=payload)
    assert assert_login_schema(response.json()) == True
    assert response.status_code == 200
    assert_login_success(response.json())


def test_login_without_client_secret():
    url = f'{system_url}{Endpoints.login.value}'
    payload = {'client_id': f'{client_id}', 'grant_type': f'{grant_type}'}
    response = requests.post(url=url, data=payload)
    response_data = response.json()
    assert response.status_code == 400
    assert response_data["error"] == "invalid_client"
    assert response_data["error_description"] == "client credentials are required"


def test_login_no_credentials():
    url = f'{system_url}{Endpoints.login.value}'
    response = requests.post(url)
    response_data = response.json()
    #assert  response.status_code == 403
    #assert_login_blocked(response_data)
    assert response.status_code == 400
    assert_login_failed(response_data)


def test_without_client_id():
    url = f'{system_url}{Endpoints.login.value}'
    payload = {'client_secret': f'{client_secret}', 'grant_type': f'{grant_type}'}
    response = requests.post(url=url, data=payload)
    response_data = response.json()
    #assert response.status_code == 403
    #assert_login_blocked(response_data)
    assert response_data["error"] == "invalid_client"
    assert response_data["error_description"] == "Client credentials were not found in the headers or body"

def test_without_grant_type():
    url = f'{system_url}{Endpoints.login.value}'
    payload = {'client_id': f'{client_id}', 'client_secret': f'{client_secret}'}
    response = requests.post(url=url, data=payload)
    response_data = response.json()
    #assert response.status_code == 403
    #assert_login_blocked(response_data)
    assert response.status_code == 400
    assert_login_failed(response_data)




