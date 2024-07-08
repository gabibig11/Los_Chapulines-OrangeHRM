import json

import pytest
import requests
from config import system_url
from src.assertions.login_assertions import assert_login_success
from src.orangeHRM_api.api_requests import OrangeRequests
from src.orangeHRM_api.endpoints import Endpoints


@pytest.fixture (scope='session')
def test_login():
    url = f'{system_url}{Endpoints.login.value}'
    payload = {'client_id': 'api-client', 'client_secret': '942d36a36d6bf422a36f5871f905b6e5',
               'grant_type': 'client_credentials'}
    response = OrangeRequests().post(url=url, data=payload)
    response_data=response.json()
    assert response.status_code == 200
    assert_login_success(response_data)
    token = f'{response_data["token_type"]} {response_data["access_token"]}'
    def login_teardown():
        print("Token eliminado")

    yield token
    login_teardown()
    #return token


def post_teardown(url, headers, response, attribute_search, attribute_delete, array=None):
    # Obtenemos el id del objeto
    id=str(response['data'][attribute_search])
    #Obtener la concadenacion del atributo que se necesita para borrar y el id
    #El parametro array no es necesario pasarlo
    json_value=([id] if array==True else id)
    payload = {attribute_delete: json_value}
    #response_delete = OrangeRequests().delete(url=url, headers=headers, data= json.dumps(payload))
    response_delete = OrangeRequests().delete(url=url, headers=headers, data=payload)
    assert response_delete.status_code == 204



