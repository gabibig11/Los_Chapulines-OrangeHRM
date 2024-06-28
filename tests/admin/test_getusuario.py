import requests
import pytest
from conftest import system_url

def test_get_users(test_login):
	token=test_login
	url = f'{system_url}/api/systemUsers/100'
	payload = {}
	headers = {
  	 'Authorization': f'Bearer {token}'
	}
	response = requests.get(url, headers=headers, data=payload)
	response_data = response.json()
	assert response.status_code == 200