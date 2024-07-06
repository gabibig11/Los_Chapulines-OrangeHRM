import json
import pytest
from conftest import *
from src.assertions.location_assertions import *
from src.orangeHRM_api.endpoints import Endpoints

#Verificar que se pueda agregar un status laboral
@pytest.mark.smoke7
def test_employment_status_add(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = json.dumps({

            "name": "Martina"
        })

    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 201
    #response_json = response.json()
    post_teardown(url=url, headers=headers, response=response, attribute="data")


#erificar si se puede agregar un status laboras con un toquen expirado
def test_expired_token():

    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Authorization': 'Bearer 6e81dcf8cd0f3651d393f712e6ee332b30a4ed2d'}
    response = OrangeRequests().post(url, headers=headers)
    assert response.status_code == 401

#Verificar que no se pueda agregar un status laboral con más de 60 caracteres

