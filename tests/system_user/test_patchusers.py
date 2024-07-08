import requests
import pytest
from config import system_url
from src.assertions.patchusers_assertions import *
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests


@pytest.mark.elupdate
def test_patchusers_success(test_login, setup_patchusers): # test1 editar un usuario existente del sistema
    token=test_login
    user_id=setup_patchusers
    url = f'{system_url}{Endpoints.patchusers.value}{user_id}'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {
        "essrole": "2",
        "supervisorrole": "3",
        "changepassword": "true",
        "password": "albertitoTest13",
        "confirmpassword": "albertitoTest13"
    }
    assert_patchusers_payload_schema(payload)
    response=OrangeRequests().patch(url=url, headers=headers, data=payload)
    response_data=response.json()
    assert response.status_code==200
    assert_patchusers_schema(response_data)
    assert response_data['messages']['success']=='Successfully Saved'