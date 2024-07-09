import json
import secrets

import pytest
from config import system_url
from src.assertions.getcustomer_assertions import *
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests
from conftest import *

@pytest.mark.smoke
def test_getcustomer_success(test_login): # test1 obtener el cliente por su id
    id='17'
    token = test_login
    url = f'{system_url}{Endpoints.getcustomer.value}{id}'
    headers = {'Authorization': token}
    response = OrangeRequests().get(url=url, headers=headers)
    response_data = response.json()
    assert response.status_code == 200
    assert_getcustomer_schema(response_data)

def test_getcustomer_without_id(test_login): # test2 error al no proporcionar un id
    id=''
    token = test_login
    url = f'{system_url}{Endpoints.getcustomer.value}{id}'
    headers = {'Authorization': token}
    response = OrangeRequests().get(url=url, headers=headers)
    response_data = response.json()
    assert response.status_code == 401

def test_getcustomer_invalid_id(test_login): # test3 error al proporcionar un id invalido
    id='invalid'
    token = test_login
    url = f'{system_url}{Endpoints.getcustomer.value}{id}'
    headers = {'Authorization': token}
    response = OrangeRequests().get(url=url, headers=headers)
    response_data = response.json()
    assert response.status_code == 422
    assert "Invalid Data Submitted" in response_data['message']

def test_getcustomer_non_existant_id(test_login): # test4 error al proporcionar un id inexistente
    id='10000'
    token = test_login
    url = f'{system_url}{Endpoints.getcustomer.value}{id}'
    headers = {'Authorization': token}
    response = OrangeRequests().get(url=url, headers=headers)
    response_data = response.json()
    assert response.status_code == 404
    assert "Not Found" in response_data['message']

@pytest.mark.xfail(reason="Error de schema de respuesta que no contiene los detalles esperados al proporcionar el parametro 'include=CostCentre'-HU706-Verificar que la API devuelve la información de los clientes con más detalles al proporcionar el parámetro y valor “include=CostCentre”")
def test_getcustomer_with_include(test_login): # test5 obtener informacion del cliente con mas detalles al proporcionar el parametro include
    id='17'
    token = test_login
    url = f'{system_url}{Endpoints.getcustomer.value}{id}'
    headers = {'Authorization': token}
    params = {
        "include": "CostCentre"
    }
    response = OrangeRequests().get(url=url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getcustomer_include_schema(response_data)


def test_getcustomer_invalid_param(test_login): # test6 error al proporcionar un parametro invalido
    id='17'
    token = test_login
    url = f'{system_url}{Endpoints.getcustomer.value}{id}'
    headers = {'Authorization': token}
    params = {
        "invalidParam": "invalid"
    }
    response = OrangeRequests().get(url=url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 422
    assert "Invalid Data Submitted" in response_data['message']


def test_getcustomer_invalid_value_into_include(test_login): # test7 error al proporcionar un valor invalido para el parametro include
    id='17'
    token = test_login
    url = f'{system_url}{Endpoints.getcustomer.value}{id}'
    headers = {'Authorization': token}
    params = {
        "include": "invalid"
    }
    response = OrangeRequests().get(url=url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 422
    assert "Invalid Data Submitted" in response_data['message']


def test_getcustomer_invalid_token(test_login): # test8 error al proporcionar un token invalido
    id='17'
    token = f'Bearer {secrets.token_hex(16)}'
    url = f'{system_url}{Endpoints.getcustomer.value}{id}'
    headers = {'Authorization': token}
    params = {
        "invalidParam": "invalid"
    }
    response = OrangeRequests().get(url=url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 401



