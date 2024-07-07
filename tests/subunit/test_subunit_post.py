import json
import pytest
from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests

#Agregar una nueva subunidad con todos los campos válidos
def test_add_subunit_with_valid_data(test_login):
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Authorization': f'{test_login}', 'Content-Type': 'application/json'}
    response = OrangeRequests().post(url=url, headers=headers, data=json.dumps(valid_payload))
    assert response.status_code == 201
    response_data = response.json()
    assert response_data['data']['name'] == valid_payload['name']

    post_teardown(url, headers, response, "id")

#Agregar una nueva subunidad sin el campo 'head_of_department_employee'
def test_add_subunit_without_head_of_department_employee(test_login):
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Authorization': f'{test_login}', 'Content-Type': 'application/json'}
    response = OrangeRequests().post(url=url, headers=headers, data=json.dumps(invalid_payloads['missing_head_of_department_employee']))
    assert response.status_code == 201
    response_data = response.json()
    assert response_data['data']['name'] == invalid_payloads['missing_head_of_department_employee']['name']

    post_teardown(url, headers, response, "id")

#Agregar una nueva subunidad con el campo 'name' vacío
def test_add_subunit_with_empty_name(test_login):
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Authorization': f'{test_login}', 'Content-Type': 'application/json'}
    response = OrangeRequests().post(url=url, headers=headers, data=json.dumps(invalid_payloads['empty_name']))
    assert response.status_code == 400

#Agregar una nueva subunidad con un token de acceso inválido
def test_add_subunit_with_invalid_token():
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Authorization': 'Bearer invalid_token', 'Content-Type': 'application/json'}
    response = OrangeRequests().post(url=url, headers=headers, data=json.dumps(valid_payload))
    assert response.status_code == 401

#Agregar nueva subunidad con un token de acceso vacío
def test_add_subunit_with_empty_token():
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Authorization': '', 'Content-Type': 'application/json'}
    response = OrangeRequests().post(url=url, headers=headers, data=json.dumps(valid_payload))
    assert response.status_code == 401
