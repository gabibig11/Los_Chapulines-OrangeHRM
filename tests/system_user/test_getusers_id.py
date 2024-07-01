import requests
import pytest
from config import system_url
from src.assertions.getusers_assertions import assert_getusers_id_schema, assert_getusers_id_include_schema
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests

def test_get_users_id(test_login):#test1 usuario por id
	token=test_login
	user_id='100'
	url = f'{system_url}{Endpoints.getusers_id.value}{user_id}'
	headers = {'Authorization': token}
	#response = requests.get(url, headers=headers, data=payload)
	response= OrangeRequests().get(url, headers=headers)
	response_data = response.json()
	assert response.status_code == 200
	assert_getusers_id_schema(response_data)

def test_get_users_id_include(test_login):#test3 usuario por id con parametro include
	token = test_login
	user_id = '100'
	url = f'{system_url}{Endpoints.getusers_id.value}{user_id}'
	params = {
		'include': 'Employee,UserUserRole,UserRole,Regions'
	}
	headers = {'Authorization': token}
	#response = requests.get(url, headers=headers, params=params, data=payload)
	response = OrangeRequests().get(url, headers=headers, params=params)
	response_data = response.json()
	assert response.status_code == 200
	assert_getusers_id_include_schema(response_data)

def test_get_users_invalid_id(test_login):#test2 error por id invalido
	token = test_login
	user_id = '1000'
	url = f'{system_url}{Endpoints.getusers_id.value}{user_id}'
	headers = {'Authorization': token}
	response = OrangeRequests().get(url, headers=headers)
	assert response.status_code == 403

@pytest.mark.xfail
def test_get_users_id_not_supported_params(test_login):#test4 error por parametro no soportado FAILED
	token = test_login
	user_id = '100'
	url = f'{system_url}{Endpoints.getusers_id.value}{user_id}'
	params = {
		'includeParam': 'Employee,UserUserRole,UserRole,Regions'
	}
	headers = {'Authorization': token}
	response = OrangeRequests().get(url, headers=headers, params=params)
	assert response.status_code == 400

def test_get_users_id_invalid_token():#test5 error por token invalido
	token = '7ae27d28b1a8e0379cf4f1f5adf2cd3aa4713308'
	user_id = '100'
	url = f'{system_url}{Endpoints.getusers_id.value}{user_id}'
	headers = {'Authorization': token}
	response = OrangeRequests().get(url, headers=headers)
	assert response.status_code == 401

def test_get_users_id_without_token():#test6 error por falta de token
	token = ''
	user_id = '100'
	url = f'{system_url}{Endpoints.getusers_id.value}{user_id}'
	headers = {'Authorization': token}
	response = OrangeRequests().get(url, headers=headers)
	assert response.status_code == 401