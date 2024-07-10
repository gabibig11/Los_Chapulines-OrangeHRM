from config import *
from conftest import *
from src.orangeHRM_api.api_requests import OrangeRequests
from src.orangeHRM_api.endpoints import Endpoints
from src.assertions.location_assertions import *
from src.resources.functions.location import *


def test_location_delete_success(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}

    object= object_random(url=url, headers=headers)
    id_object= id_object_value(object)
    payload = {"data": [id_object]}

    assert assert_location_schema_delete_input(payload) == True
    response= OrangeRequests().delete(url=url, headers=headers, data=payload)
    assert response.status_code == 204

    data_post= clean_data_location(object)
    delete_teardown(url=url, headers=headers, body=data_post)

@pytest.mark.xfail (reason= "Error al enviar un json con el campo id vacio H403-Verificar el error al ingresar el campo id vacio" )
def test_location_delete_message_field_id_empty(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload= {"data":[]}
    assert assert_location_schema_delete_input(payload) == False
    response = OrangeRequests().delete(url=url, headers=headers, data=payload)
    assert response.status_code== 400

def test_location_delete_id_invented(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload= {"data": ["100"]}
    assert assert_location_schema_delete_input(payload) == True
    response = OrangeRequests().delete(url=url, headers=headers, data=payload)
    assert response.status_code == 500

def test_location_delete_token_invented():
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{random_token}'}
    payload = {"data": ["1"]}
    assert assert_location_schema_delete_input(payload) == True
    response = OrangeRequests().delete(url=url, headers=headers, data=payload)
    assert response.status_code == 401

def test_location_delete_without_token():
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json'}
    payload = {"data": ["1"]}
    assert assert_location_schema_delete_input(payload) == True
    response = OrangeRequests().delete(url=url, headers=headers, data=payload)
    assert response.status_code == 401

def test_location_delete_token_expired():
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{expired_token}'}
    payload = {"data": ["1"]}
    assert assert_location_schema_delete_input(payload) == True
    response = OrangeRequests().delete(url=url, headers=headers, data=payload)
    assert response.status_code == 401