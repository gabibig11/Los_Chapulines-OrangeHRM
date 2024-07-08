import json
import pytest
from config import system_url
from src.assertions.postcustomer_assertions import *
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests
from conftest import *
import secrets

@pytest.mark.smoke
def test_postcustomer_success(test_login): # test1 agrega un cliente nuevo en base al body de ejemplo
    token = test_login
    url = f'{system_url}{Endpoints.postcustormer.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload ={
        "name": "Jalasoft Company",
        "description": "Software developer company"
    }
    data=json.dumps(payload)
    assert_postcustomer_payload_schema(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    response_data = response.json()
    assert response.status_code == 201
    assert_postcustomer_schema(response_data)
    customerId = response_data['data']['customerId']
    #print(vacancyId)
    #print(response_data)
    post_teardown_diego(url=url, headers=headers, value=customerId, attribute='ids', array=True)


def test_postcustomer_not_supported_properties(test_login): # test2 error al agregar un cliente nuevo con propiedades no soportadas
    token = test_login
    url = f'{system_url}{Endpoints.postcustormer.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload ={
        "name": "Jalasoft Company",
        "description": "Software developer company",
        "invalidPropertie": "invalid"
    }
    data=json.dumps(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    response_data = response.json()
    assert response.status_code == 422
    assert response_data['message'] == 'Invalid Data Submitted'

def test_postcustomer_name_already_exists(test_login): # test3 error al agregar un cliente nuevo con "name" ya existente
    token = test_login
    url = f'{system_url}{Endpoints.postcustormer.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload ={
        "name": "Apache Software Foundation",
        "description": "Software developer company"
    }
    data=json.dumps(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    response_data = response.json()
    assert response.status_code == 409

@pytest.mark.xfail(reason="Error al agregar cliente con propiedad 'costeCentreId'-HU705-Verificar que la API agrega un cliente nuevo cuando se proporciona la propiedad opcional “costCentreId” ")
def test_postcustomer_whith_costCentreId_propertie(test_login):  # test4 agregar un cliente nuevo con "costCentreId"
    token = test_login
    url = f'{system_url}{Endpoints.postcustormer.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "name": "Jalasoft Company",
        "description": "Software developer company",
        "costCentreId": "1"
    }
    data = json.dumps(payload)
    assert_postcustomer_payload_schema(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    response_data = response.json()
    assert response.status_code == 201
    assert_postcustomer_schema(response_data)
    customerId = response_data['data']['customerId']
    post_teardown_diego(url=url, headers=headers, value=customerId, attribute='ids', array=True)

def test_postcustomer_whith_costCentreId_propertie_invalid(test_login):  # test5 error al agregar un cliente nuevo con "costCentreId" con valor invalido
    token = test_login
    url = f'{system_url}{Endpoints.postcustormer.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "name": "Jalasoft Company",
        "description": "Software developer company",
        "costCentreId": "invalid"
    }
    data = json.dumps(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    response_data = response.json()
    assert response.status_code == 422
    assert response_data['message'] == 'Invalid Data Submitted'

@pytest.mark.xfail(reason="Error al agregar cliente con propiedad 'costeCentreId' e 'include=CostCentre' en el url-HU705-Verificar que la API agrega un nuevo cliente con la propiedad 'costCentreId' cuando se usa el parámetro 'include' en el url.")
def test_postcustomer_whith_costCentreId_propertie_and_include(test_login):  # test6 agregar un cliente nuevo con "costCentreId" e include=CostCentre en el url
    token = test_login
    url = f'{system_url}{Endpoints.postcustormer.value}?include=CostCentre'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "name": "Jalasoft Company",
        "description": "Software developer company",
        "costCentreId": "1"
    }
    data = json.dumps(payload)
    assert_postcustomer_payload_schema(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    response_data = response.json()
    assert response.status_code == 201
    assert_postcustomer_schema(response_data)
    customerId = response_data['data']['customerId']
    post_teardown_diego(url=url, headers=headers, value=customerId, attribute='ids', array=True)

def test_postcustomer_whith_costCentreId_propertie_invalid_and_inlclude(test_login):  # test7 agregar un cliente nuevo con "costCentreId" con valor invalido e include=CostCentre en el url
    token = test_login
    url = f'{system_url}{Endpoints.postcustormer.value}?include=CostCentre'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "name": "Jalasoft Company",
        "description": "Software developer company",
        "costCentreId": "invalid"
    }
    data = json.dumps(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    response_data = response.json()
    assert response.status_code == 422
    assert response_data['message'] == 'Invalid Data Submitted'

def test_postcustomer_invalid_token(): # test8 error al agregar un cliente con token invalido
    token = f'Bearer {secrets.token_hex(16)}'
    url = f'{system_url}{Endpoints.postvacancy.value}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "name": "Jalasoft Company",
        "description": "Software developer company"
    }
    data=json.dumps(payload)
    assert_postcustomer_payload_schema(payload)
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    assert response.status_code == 401






