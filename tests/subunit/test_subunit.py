import requests
import pytest
import json
from jsonschema import validate
from config import system_url
from src.orangeHRM_api.endpoints import Endpoints

# Del esquema JSON
with open('src/resources/schemas/subunit_schema.json') as schema_file:
    subunit_schema = json.load(schema_file)



@pytest.mark.smoke #para definir cual es mi test smoke
def test_get_subunit_valid_id(test_login):
    subunit_id = 1
    url = f'{system_url}{Endpoints.subunits.value}/{subunit_id}'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['data']['id'] == str(subunit_id)

def test_get_subunit_invalid_token():
    subunit_id = 1
    url = f'{system_url}{Endpoints.subunits.value}/{subunit_id}'
    headers = {'Authorization': 'Bearer invalid_token'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 401

def test_get_subunit_no_token():
    subunit_id = 1
    url = f'{system_url}{Endpoints.subunits.value}/{subunit_id}'
    response = requests.get(url)
    assert response.status_code == 401

def test_get_subunit_not_found(test_login):
    subunit_id = 9999  # Assuming this ID does not exist
    url = f'{system_url}{Endpoints.subunits.value}/{subunit_id}'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 404

def test_get_subunits_list(test_login):
    url = f'{system_url}{Endpoints.subunits.value}'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    validate(instance=response_data, schema=subunit_schema)

def test_get_subunits_with_name_filter(test_login):
    url = f'{system_url}{Endpoints.subunits.value}?fields[]=name'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert 'data' in response_data
    for subunit in response_data['data']:
        assert 'name' in subunit

def test_get_subunits_with_cost_centre_id_filter(test_login):
    url = f'{system_url}{Endpoints.subunits.value}?fields[]=cost_centre_id'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert 'data' in response_data
    for subunit in response_data['data']:
        assert 'cost_centre_id' in subunit

def test_get_subunits_sorted_asc(test_login):
    url = f'{system_url}{Endpoints.subunits.value}?sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert 'data' in response_data

def test_get_subunits_sorted_desc(test_login):
    url = f'{system_url}{Endpoints.subunits.value}?sortingOrder=DESC'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert 'data' in response_data



def test_get_subunits_invalid_request(test_login):
    url = f'{system_url}{Endpoints.subunits.value}?invalid_param=true'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 400 or response.status_code == 200
