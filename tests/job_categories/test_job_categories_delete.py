import pytest
from config import system_url, random_token, expired_token
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests
from src.assertions.job_categories_assertions import assert_job_categories_delete, assert_delete_job_categories_schema

@pytest.mark.smoke
def test_job_categories_delete(test_login):

    data = {
        "name" : "fake job category3"
    }

    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    response_json = response.json()
    response_data = response_json["data"]
    created_id=response_data["id"]
    payload={"data" : [created_id]}
    # assert assert_delete_job_categories_schema(payload) == True
    response_delete = OrangeRequests().delete(url=url, headers=headers, data=payload)
    
    assert_job_categories_delete(response_delete)


def test_job_categories_delete_id_invalido(test_login):
    payload={
        "data" : ["id_invalido"]
    }

    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().delete(url, headers=headers, data=payload)
    assert response.status_code == 400


def test_job_categories_delete_without_id(test_login):
    payload={
        "data" : [""]
    }

    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().delete(url, headers=headers, data=payload)
    assert response.status_code == 400


def test_job_categories_delete_invalid_token():
    payload={
        "data" : ["5"]
    }
     
    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{random_token}'}
    response = OrangeRequests().delete(url, headers=headers, data=payload)
    assert response.status_code == 401


def test_job_categories_delete_expired_token():
    payload={
        "data" : ["5"]
    }
     
    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{expired_token}'}
    response = OrangeRequests().delete(url, headers=headers, data=payload)
    assert response.status_code == 401