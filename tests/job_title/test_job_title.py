import os
import pytest
import sys
import requests
import jsonschema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests


def test_job_title_success(test_login):  # repuesta exitosa al solicitar todos los cargos que estan aqui
    url = f'{system_url}{Endpoints.job_titles.value}'
    # url = 'https://api-sandbox.orangehrm.com/api/jobTitles'
    print(test_login)
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['data']is not None

def test_job_title_no_token(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    response = requests.get(url)
    response_err = response.json()
    assert response.status_code == 401
    assert response_err == []  # suposicion


def test_job_title_invalid_token(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': f'Bearer 519ba4b405aca163fb4c7740868884a37ff34d'}  # 519ba4b405aca163fb4c7740868884a37ff34d
    response = requests.get(url, headers=headers)
    response_err = response.json()
    assert response.status_code == 401
    assert response_err['error'] == "invalid_token"
    assert response_err['error_description'] == "The access token provided is invalid"


def test_job_title_expired_token(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': f'Bearer da8c7430701fd54d0582de569b6fb3859c9a0fd0'}  # da8c7430701fd54d0582de569b6fb3859c9a0fd0
    response = requests.get(url, headers=headers)
    response_err = response.json()
    assert response.status_code == 401
    assert response_err['error'] == "expired_token"
    assert response_err['error_description'] == "The access token provided has expired"


def test_job_title_incomplete_header():
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': 'Bearer'}  # la estructura de header empieza con Bearer acompañado del token
    response = requests.get(url, headers=headers)
    response_data = response.json()
    assert response.status_code == 401
    assert response_data["error"] == 'invalid_request'
    assert response_data["error_description"] == "Malformed auth header"


def test_schema_job(test_login):
    url = f'{system_url}/api/jobTitles?limit=1&offset=0&sortingField=id&sortingOrder=ASC'  # formato correcto
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_schema = response.json()
    print(response_schema)
    schema = {
        "type": "object",
        "properties": {
            "data": {
                "type": "array",
                "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "jobTitleName": {
                                "type": "string"
                            },
                            "jobDescription": {
                                "type": "string"
                            },
                            "note": {
                                "type": "string"
                            },
                            "isDeleted": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "jobTitleName",
                            "jobDescription",
                            "note",
                            "isDeleted"
                        ]
                }
            },
            "meta": {
                "type": "object",
                "properties": {
                    "total": {
                        "type": "integer"
                    }
                },
                "required": [
                    "total"
                ]
            }
        },
        "required": [
            "data",
            "meta"
        ]
    }
    try:
        jsonschema.validate(instance=response_schema, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'pruebaError {err}')
    assert response.status_code == 200


def test_job_title_not_empty_labels(test_login):
    url = f'{system_url}/api/jobTitles?limit=1&offset=0&sortingField=id&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_data = response.json()
    for job_object in response_data['data']:
        assert job_object['id'] is not None
        assert job_object['jobTitleName'] is not None
        assert job_object['jobDescription'] is not None
        assert job_object['note'] is not None
        assert job_object['isDeleted'] is not None


def test_job_title_sortingField(test_login):
    url = f'{system_url}/api/jobTitles?sortingField=id'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_data = response.json()
    assert response_data['data'] is not None


def test_job_title_sortingOrder_desc(test_login):
    url = f'{system_url}/api/jobTitles?sortingField=id&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_data = response.json()
    assert response_data['data'] is not None


def test_job_title_params(test_login):
    url = f'{system_url}/api/jobTitles?limit=10&offset=0&sortingField=id&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_data = response.json()
    assert response_data['data'] is not None


def test_job_title_invalid_params(test_login):
    url = f'{system_url}/api/jobTitles?limit=10&offset=0&sortingField=id&order=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 400

