import pytest
from config import system_url, random_token, expired_token
from src.orangeHRM_api.endpoints import Endpoints
from conftest import delete_teardown
from conftest import test_login
from src.orangeHRM_api.api_requests import OrangeRequests
from src.assertions.employment_status_assertions import *
from src.resources.functions.employment_status import set_up_delete

@pytest.mark.smoke
def test_employment_status_delete(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Authorization': f'{test_login}'}
    data_to_delete = set_up_delete(test_login)
    id_to_delete = data_to_delete.pop('id', None)
    assert id_to_delete is not None
    payload_to_delete={"data" : [id_to_delete]}
    assert_delete_employment_status_schema(payload_to_delete)
    response_delete = OrangeRequests().delete(url=url, headers=headers, data=payload_to_delete)
    assert_employment_status_delete(response_delete)
    delete_teardown(url, headers=headers, body=data_to_delete)

def test_employment_status_delete_id_invalid(test_login):
    payload = {
        "data": ["id_invalid"]
    }

    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().delete(url, headers=headers, data=payload)
    assert response.status_code == 400


def test_employment_status_delete_invalid_token():
    payload = {
        "data": ["1"]
    }

    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Authorization': f'{random_token}'}
    response = OrangeRequests().delete(url, headers=headers, data=payload)
    assert response.status_code == 401


def test_employment_status_delete_expired_token():
    payload = {
        "data": ["1"]
    }

    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Authorization': f'{expired_token}'}
    response = OrangeRequests().delete(url, headers=headers, data=payload)
    assert response.status_code == 401