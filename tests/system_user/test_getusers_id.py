import requests
import pytest
from config import system_url
from src.assertions.getusers_id_assertions import assert_getusers_id_schema, assert_getusers_id_include_schema
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests

def test_get_users_id(test_login):#test case 1
	token=test_login
	user_id='100'
	url = f'{system_url}{Endpoints.getusers_id.value}{user_id}'
	headers = {'Authorization': f'{token}'}
	#response = requests.get(url, headers=headers, data=payload)
	response= OrangeRequests().get(url, headers=headers)
	response_data = response.json()
	assert response.status_code == 200
	assert_getusers_id_schema(response_data)

def test_get_users_id_include(test_login):#test case 3
	token = test_login
	user_id = '100'
	url = f'{system_url}{Endpoints.getusers_id.value}{user_id}'
	params = {
		'include': 'Employee,UserUserRole,UserRole,Regions'
	}
	headers = {'Authorization': f'{token}'}
	#response = requests.get(url, headers=headers, params=params, data=payload)
	response = OrangeRequests().get(url, headers=headers, params=params)
	response_data = response.json()
	assert response.status_code == 200
	assert_getusers_id_include_schema(response_data)
