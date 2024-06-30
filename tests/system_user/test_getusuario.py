import requests
import pytest
from conftest import system_url

def test_get_users_id(test_login):
	token=test_login
	url = f'{system_url}/api/systemUsers/100'
	payload = {}
	headers = {
  	 'Authorization': f'Bearer {token}'
	}
	response = requests.get(url, headers=headers, data=payload)
	response_data = response.json()
	assert response.status_code == 200

def test_get_users_id_include(test_login):
	token = test_login
	url = f'{system_url}/api/systemUsers/100'
	params = {
		'include': 'Employee,UserUserRole,Regions'
	}
	payload = {}
	headers = {
		'Authorization': f'Bearer {token}'
	}
	response = requests.get(url, headers=headers, params=params, data=payload)
	response_data = response.json()
	assert response.status_code == 200
