import json
import pytest
from conftest import *
from src.assertions.employment_status_assertions import *
from config import system_url, random_token, expired_token
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests
from conftest import post_teardown

#1Verificar que se pueda agregar un status laboral
@pytest.mark.smoke
def test_employment_status_add(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Authorization': f'{test_login}'}
    payload = {

            "name": "karokkarol"
        }
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 201
    post_teardown(url=url, headers=headers, response=response.json(), attribute_search="id", attribute_delete="data",
                  array=True)

#2Verificar que no se pueda agregar un status que ya esta agregado
def test_employment_status_already_added(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {

        "name": "maritzaillanesqqq"
    }

    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400

#3Verificar que no se pueda agregar un status laboral con más de 60 caracteres

@pytest.mark.xfail(reason="agrega un status con mas de 60 caracteres")
def test_employment_60_characters(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {

        "name": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    }

    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 500

#4Verificar que no se pueda agregar un estatus laboral de cero caracteres
@pytest.mark.xfail(reason="agrega un status con 0 caracteres")
def test_employment_0_characters(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {

        "name": " "
    }

    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 500

#5Verificar que no se pueda agregar un status laboral de un carácter
@pytest.mark.xfail(reason="agrega un status con 1 caracteres")
def test_employment_1_characters(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {

        "name": "a"
    }

    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 500

#6Verificar que no se acepte un numero al agregar un status laboral
@pytest.mark.xfail(reason="agrega un status con caracteres numericos")
def test_employment_1_characters(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {

        "name": "123"
    }

    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 500
#7Verificar que no se acepte caracteres especiales al agregar un status laboral

@pytest.mark.xfail(reason="agrega un status con caracteres especiales")
def test_employment_special_characters(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {

        "name": "@"
    }

    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 500

