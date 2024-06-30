import requests
from tests.config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.utils.load_resources import load_schema_resource
import jsonschema
import pytest


@pytest.mark.smoke
def test_job_categories_schema_file(test_login):
    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_json = response.json()

    schema = load_schema_resource("job_categories_schema.json")
    assert jsonschema.validate(instance=response_json, schema=schema) is None


def test_job_categories_success(test_login):
    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['data'] is not None


def test_job_categories_filter_by_limit(test_login):
    limit = 5
    # sortingFeild is requiret to use limit filter
    url = f'{system_url}{Endpoints.job_categories.value}?limit={limit}&sortingFeild=id'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json['data']) == limit


def test_job_categories_filter_by_field(test_login):
    url = f'{system_url}{Endpoints.job_categories.value}?limit=10&sortingFeild=id'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    response_data = response_json["data"]
    assert response.status_code == 200
    assert all([int(response_data[i]["id"]) > int(response_data[i+1]["id"]) for i in range(len(response_data) - 1)])


def test_job_categories_filter_by_field_and_order(test_login):
    url = f'{system_url}{Endpoints.job_categories.value}?limit=10&sortingFeild=id&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    response_data = response_json["data"]
    assert response.status_code == 200
    assert all([int(response_data[i]["id"]) < int(response_data[i+1]["id"]) for i in range(len(response_data) - 1)])


def test_job_categories_invalid_filter(test_login):
    url = f'{system_url}{Endpoints.job_categories.value}?invalidFilter=invalidFilterValue'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 400
