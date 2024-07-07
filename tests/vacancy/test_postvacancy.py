import json
import pytest
from config import system_url
from src.assertions.postvacancy_assertions import *
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests
from conftest import *
import secrets



def test_postvacancy_success(test_login): # test1 agrega una vacante nueva en base al body de ejemplo
    token = test_login
    url = f'{system_url}{Endpoints.postvacancy.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload ={
        "copyFromTemplate": "false",
        "vacancyName": "software engineer 2022",
        "location": "15",
        "subUnit": "23",
        "jobTitle": "278",
        "noOfPositions": "2",
        "hiringManager": ["68", "25"],
        "resumeRequired": "true",
        "requestConsent": "false"
    }
    assert_postvacancy_payload_schema(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 201
    assert_postvacancy_schema(response_data)
    vacancyId = response_data['data']['vacancyId']
    #print(vacancyId)
    #print(response_data)
    post_teardown(url=url, headers=headers, value=vacancyId, attribute='ids', array=True)

def test_postvacancy_success_resumeRequired_modified(test_login): # test2 agrega una vacante nueva en base al body de ejemplo con "resumeRequired" con "false"
    token = test_login
    url = f'{system_url}{Endpoints.postvacancy.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "copyFromTemplate": "false",
        "vacancyName": "software engineer 2022",
        "location": "15",
        "subUnit": "23",
        "jobTitle": "278",
        "noOfPositions": "2",
        "hiringManager": ["68", "25"],
        "resumeRequired": "false",
        "requestConsent": "false"
    }
    assert_postvacancy_payload_schema(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 201
    assert_postvacancy_schema(response_data)
    vacancyId = response_data['data']['vacancyId']
    post_teardown(url=url, headers=headers, value=vacancyId, attribute='ids', array=True)

def test_postvacancy_success_requestConsent_modified(test_login): # test3 agrega una vacante nueva en base al body de ejemplo con "requestConsent" con "true"
    token = test_login
    url = f'{system_url}{Endpoints.postvacancy.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "copyFromTemplate": "false",
        "vacancyName": "software engineer 2022",
        "location": "15",
        "subUnit": "23",
        "jobTitle": "278",
        "noOfPositions": "2",
        "hiringManager": ["68", "25"],
        "resumeRequired": "true",
        "requestConsent": "true"
    }
    assert_postvacancy_payload_schema(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 201
    assert_postvacancy_schema(response_data)
    vacancyId = response_data['data']['vacancyId']
    post_teardown(url=url, headers=headers, value=vacancyId, attribute='ids', array=True)

@pytest.mark.negative
def test_postvacancy_whithout_values(test_login): # test4 error al agregar una vacante nueva con propiedades con valores vacios
    token = test_login
    url = f'{system_url}{Endpoints.postvacancy.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "copyFromTemplate": "false",
        "vacancyName": "software engineer 2022",
        "location": "",
        "subUnit": "23",
        "jobTitle": "278",
        "noOfPositions": "",
        "hiringManager": ["68", "25"],
        "resumeRequired": "",
        "requestConsent": ""
    }
    assert_postvacancy_payload_schema(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 400
    assert_postvacancy_error_400_schema(response_data)
    assert response_data['title'] == 'Invalid data'

@pytest.mark.negative
def test_postvacancy_whith_not_supported_properties(test_login): # test5 error al agregar una vacante nueva con propiedades no soportadas
    token = test_login
    url = f'{system_url}{Endpoints.postvacancy.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "copyFromTemplate": "false",
        "vacancyName": "software engineer 2022",
        "location": "15",
        "subUnit": "23",
        "jobTitle": "278",
        "noOfPositions": "2",
        "hiringManager": ["68", "25"],
        "resumeRequired": "true",
        "requestConsent": "false",

        "NewInvalidPropertie": "Invalid"
    }
    assert_postvacancy_payload_schema(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 400
    assert_postvacancy_error_400_schema(response_data)
    assert response_data['title'] == 'Invalid data'

@pytest.mark.negative
def test_postvacancy_vacancyName_already_exists(test_login): # test6 error al agregar una vacante nueva con "vacancyName" ya existente
    token = test_login
    url = f'{system_url}{Endpoints.postvacancy.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "copyFromTemplate": "false",
        "vacancyName": "software engineer 2024 quality aasurance",
        "location": "15",
        "subUnit": "23",
        "jobTitle": "278",
        "noOfPositions": "2",
        "hiringManager": ["68", "25"],
        "resumeRequired": "true",
        "requestConsent": "false"
    }
    assert_postvacancy_payload_schema(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 400
    assert_postvacancy_error_400_schema(response_data)
    assert response_data['title'] == 'Invalid data'
    assert 'vacancyName must be unique' in response_data['details']

@pytest.mark.negative
def test_postvacancy_invalid_token(): # test7 error al agregar una vacante nueva con token invalido
    token = f'Bearer {secrets.token_hex(16)}'
    url = f'{system_url}{Endpoints.postvacancy.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "copyFromTemplate": "false",
        "vacancyName": "software engineer 2022",
        "location": "15",
        "subUnit": "23",
        "jobTitle": "278",
        "noOfPositions": "2",
        "hiringManager": ["68", "25"],
        "resumeRequired": "true",
        "requestConsent": "false"
    }
    assert_postvacancy_payload_schema(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 401

@pytest.mark.negative
def test_postvacancy_void_token(): # test8 error al agregar una vacante nueva con token con valor vacio
    token = ''
    url = f'{system_url}{Endpoints.postvacancy.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "copyFromTemplate": "false",
        "vacancyName": "software engineer 2022",
        "location": "15",
        "subUnit": "23",
        "jobTitle": "278",
        "noOfPositions": "2",
        "hiringManager": ["68", "25"],
        "resumeRequired": "true",
        "requestConsent": "false"
    }
    assert_postvacancy_payload_schema(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 401

@pytest.mark.negative
def test_postvacancy_jobTitle_non_existent_value(test_login): # test9 error al agregar una vacante nueva con "jobTitle" inexistente
    token = test_login
    url = f'{system_url}{Endpoints.postvacancy.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "copyFromTemplate": "false",
        "vacancyName": "software engineer 2022",
        "location": "15",
        "subUnit": "23",
        "jobTitle": "10000",
        "noOfPositions": "2",
        "hiringManager": ["68", "25"],
        "resumeRequired": "true",
        "requestConsent": "false"
    }
    assert_postvacancy_payload_schema(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 400
    assert_postvacancy_error_400_schema(response_data)
    assert response_data['title'] == 'Invalid data'

@pytest.mark.xfail(reason="El endpoint no funciona, error 500 Internal Server Error")
def test_postvacancy_import_from_template(test_login): # test10 agrega una vacante nueva en base a una plantilla
    token = test_login
    url = f'{system_url}{Endpoints.postvacancy.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload ={
        "copyFromTemplate": "true",
        "vacancyId" : 50,
        "importJobPostingData" : "true",
        "importWorkflow": "true",
        "vacancyName" : "software engineer 2022",
        "location": "15",
        "subUnit": "23",
        "jobTitle": "278",
        "noOfPositions" : "2",
        "hiringManager" : ["68","25"]
    }
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    #response_data = response.json()
    assert response.status_code == 201
    #vacancyId = response_data['data']['vacancyId']
    #post_teardown(url=url, headers=headers, value=vacancyId, attribute='ids', array=True)