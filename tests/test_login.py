
import requests
from config import systemURL

def test_login():
    url = f'{systemURL}/oauth/issueToken'
    #url = 'https://api-sandbox.orangehrm.com/oauth/issueToken'
    payload = {'client_id': 'api-client', 'client_secret': '942d36a36d6bf422a36f5871f905b6e5',
               'grant_type': 'client_credentials'}
    response = requests.post(url, data=payload)
    response_data = response.json()
    access_token = response_data["access_token"]
    assert response.status_code == 200
    assert response_data["token_type"] is not None
    print(f'Access Token: {access_token}')
