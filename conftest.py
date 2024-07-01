import pytest
import requests
from config import system_url
from src.orangeHRM_api.endpoints import Endpoints

#system_url = "https://api-sandbox.orangehrm.com"
@pytest.fixture
def test_login():
    url = f'{system_url}{Endpoints.login.value}'
    #url = f'{system_url}/oauth/issueToken'
    # url = 'https://api-sandbox.orangehrm.com/oauth/issueToken'
    payload = {'client_id': 'api-client', 'client_secret': '942d36a36d6bf422a36f5871f905b6e5',
               'grant_type': 'client_credentials'}
    response = requests.post(url, data=payload)
    response_data = response.json()
    # access_token = response_data["access_token"]
    assert response.status_code == 200
    assert response_data["token_type"] is not None
    assert response_data["access_token"] is not None
    return f'{response_data["token_type"]} {response_data["access_token"]}'
