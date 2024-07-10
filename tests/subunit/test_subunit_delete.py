import pytest

import json

from config import system_url, random_token, expired_token
from conftest import delete_teardown
from src.assertions.subunit_assertions import assert_subunit_delete_schema, assert_subunit_auth_error
from src.orangeHRM_api.api_requests import OrangeRequests
from src.orangeHRM_api.endpoints import Endpoints
from src.resources.functions.subunit import set_up_delete
from src.resources.functions.subunit import random_info


@pytest.mark.xfail
@pytest.mark.smoke
def test_subunit_delete_success(test_login):
    login = test_login
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{login}'}
    payload_id = set_up_delete(login=login)
    payload = {"data": [payload_id[0]]}
    print(payload)
    assert assert_subunit_delete_schema(payload) == True
    response = OrangeRequests().delete(url, headers=headers, data=payload)
    assert response.status_code == 200
    data = payload_id[1]
    print(data)
    delete_teardown(url, headers=headers, body=data)

def test_subunit_delete_invalid_token():
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {random_token}'}
    response = OrangeRequests().delete(url, headers=headers)
    assert response.status_code == 401
    assert_subunit_auth_error(response.json(), 1)

def test_subunit_delete_expired_token():
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': expired_token}
    response = OrangeRequests().delete(url, headers=headers)
    assert response.status_code == 401
    assert_subunit_auth_error(response.json(), 2)

def test_subunit_delete_without_token():
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Content-Type': 'application/json'}
    data = {"data": ["99"]}
    assert assert_subunit_delete_schema(data) == True
    response = OrangeRequests().delete(url, headers=headers, data=data)
    assert response.status_code == 401

@pytest.mark.xfail(reason="La petición muestra status 200 con body incorrecto - H306 - Verificar respuesta cuando se quiere hacer una petición con body incorrecto")
def test_subunit_delete_incorrect_payload(test_login):
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    data = {"id": [f'{random_info(4)}']}
    response = OrangeRequests().delete(url, headers=headers, data=data)

def test_subunit_delete_without_payload(test_login):
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    response = OrangeRequests().delete(url, headers=headers)
    assert response.status_code == 400

def test_subunit_delete_invalid_id(test_login):
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    data ={"data": [f'{random_info(4)}']}
    assert assert_subunit_delete_schema(data) == True
    response = OrangeRequests().delete(url, headers=headers, data=data)
    assert response.status_code==400