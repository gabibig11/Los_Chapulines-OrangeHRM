import secrets

import requests
import pytest
from config import system_url
from src.assertions.patchusers_assertions import *
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests


@pytest.mark.elupdate
def test_patchusers_success(test_login, setup_patchusers): # test1 editar un usuario existente del sistema
    token=test_login
    user_id=setup_patchusers
    url = f'{system_url}{Endpoints.patchusers.value}{user_id}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "user_name": "Test1",
        "essrole": "2",
        "supervisorrole": "3",
        "changepassword": "true",
        "password": "albertitoTest1",
        "confirmpassword": "albertitoTest1"
    }
    assert_patchusers_payload_schema(payload)
    response=OrangeRequests().patch(url=url, headers=headers, data=payload)
    response_data=response.json()
    assert response.status_code==200
    assert_patchusers_schema(response_data)
    assert response_data['messages']['success']=='Successfully Saved'

def test_patchusers_invalid_user(test_login): # test2 error al proporcionar un id de usuario invalido
    token=test_login
    url = f'{system_url}{Endpoints.patchusers.value}invalid'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "user_name": "Test2",
        "essrole": "2",
        "supervisorrole": "3",
        "changepassword": "true",
        "password": "albertitoTest2",
        "confirmpassword": "albertitoTest2"
    }
    assert_patchusers_payload_schema(payload)
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 401


def test_patchusers_non_existent_user(test_login): # test3 error al proporcionar un id de usuario inexistente
    token=test_login
    url = f'{system_url}{Endpoints.patchusers.value}1000'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "user_name": "Test3",
        "essrole": "2",
        "supervisorrole": "3",
        "changepassword": "true",
        "password": "albertitoTest3",
        "confirmpassword": "albertitoTest3"
    }
    assert_patchusers_payload_schema(payload)
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 404

def test_patchusers_not_supported_properties(test_login, setup_patchusers): # test4 error al proporcionar propiedades de usuario no soportados
    token=test_login
    user_id=setup_patchusers
    url = f'{system_url}{Endpoints.patchusers.value}{user_id}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "user_name": "Test4",
        "essrole": "2",
        "supervisorrole": "3",
        "changepassword": "true",
        "password": "albertitoTest4",
        "confirmpassword": "albertitoTest4",
        "invalidPropertie": "invalid"
    }
    assert_patchusers_payload_schema(payload)
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    response_data=response.json()
    assert response.status_code == 422
    assert 'Unexpected extra form field named' in response_data['errors']['general'][0]


def test_patchusers_mismatched_passwords(test_login, setup_patchusers): # test5 error al proporcionar contraseñas que no coinciden
    token=test_login
    user_id=setup_patchusers
    url = f'{system_url}{Endpoints.patchusers.value}{user_id}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "user_name": "Test5",
        "essrole": "2",
        "supervisorrole": "3",
        "changepassword": "true",
        "password": "albertitoTestCorrecto",
        "confirmpassword": "albertitoTestIncorrecto"
    }
    assert_patchusers_payload_schema(payload)
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 422
    assert 'Passwords not match' in response_data['errors']['general'][0]


def test_patchusers_user_name_already_exists(test_login, setup_patchusers): # test6 error al proporcionar un nombre de usuario ya existente
    token=test_login
    user_id=setup_patchusers
    url = f'{system_url}{Endpoints.patchusers.value}{user_id}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "user_name": "admin",
        "essrole": "2",
        "supervisorrole": "3",
        "changepassword": "true",
        "password": "albertitoTest6",
        "confirmpassword": "albertitoTest6"
    }
    assert_patchusers_payload_schema(payload)
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 409

@pytest.mark.xfail(reason="Error del endpoint que no reconoce la propiedad documentada 'changeSecondaryPassword'-HU703-Verificar que la API devuelve un error 422 cuando las contraseñas secundarias a actualizar no coinciden.")
def test_patchusers_mismatched_second_password(test_login, setup_patchusers): # test7 error al proporcionar contraseñas secundarias que no coinciden
    token=test_login
    user_id=setup_patchusers
    url = f'{system_url}{Endpoints.patchusers.value}{user_id}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "user_name": "Test7",
        "essrole": "2",
        "supervisorrole": "3",
        "changepassword": "true",
        "password": "albertitoTest7",
        "confirmpassword": "albertitoTest7",
        "changeSecondaryPassword": "true",
        "secondaryPassword": "secondPasswordCorrect",
        "confirmSecondaryPassword": "secondPasswordIncorrect"
    }
    assert_patchusers_payload_schema(payload)
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    response_data=response.json()
    print(response.json())
    assert response.status_code == 422
    assert 'Passwords not match' in response_data['errors']['general'][0]


def test_patchusers_invalid_token(test_login, setup_patchusers): # test8 error al proporcionar token invalido
    token=secrets.token_hex(16)
    user_id=setup_patchusers
    url = f'{system_url}{Endpoints.patchusers.value}{user_id}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "user_name": "Test8",
        "essrole": "2",
        "supervisorrole": "3",
        "changepassword": "true",
        "password": "albertitoTest8",
        "confirmpassword": "albertitoTest8",
    }
    assert_patchusers_payload_schema(payload)
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    response_data=response.json()
    print(response.json())
    assert response.status_code == 401
    assert 'invalid_request' in response_data['error']