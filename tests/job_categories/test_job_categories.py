from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.assertions.job_categories_assertions import assert_get_job_categories_schema, assert_get_job_categories_succesfuly
import pytest
from src.orangeHRM_api.api_requests import OrangeRequests


def test_job_categories_schema(test_login):
    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_get_job_categories_schema(response)

@pytest.mark.smoke
def test_job_categories_success(test_login):
    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    response_json = response.json()
    assert_get_job_categories_succesfuly(response)
    assert response_json['data'] is not None


def test_job_categories_filter_by_limit(test_login):
    limit = 5
    # sortingFeild is requiret to use limit filter
    url = f'{system_url}{Endpoints.job_categories.value}?limit={limit}&sortingFeild=id'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    response_json = response.json()
    assert_get_job_categories_succesfuly(response)
    assert len(response_json['data']) == limit


def test_job_categories_filter_by_field(test_login):
    url = f'{system_url}{Endpoints.job_categories.value}?limit=10&sortingFeild=id'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    response_json = response.json()
    response_data = response_json["data"]
    assert_get_job_categories_succesfuly(response)
    assert all([int(response_data[i]["id"]) > int(response_data[i+1]["id"]) for i in range(len(response_data) - 1)])


def test_job_categories_filter_by_field_and_order(test_login):
    url = f'{system_url}{Endpoints.job_categories.value}?limit=10&sortingFeild=id&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    response_json = response.json()
    response_data = response_json["data"]
    assert all([int(response_data[i]["id"]) < int(response_data[i+1]["id"]) for i in range(len(response_data) - 1)])


def test_job_categories_invalid_filter(test_login):
    url = f'{system_url}{Endpoints.job_categories.value}?invalidFilter=invalidFilterValue'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 400


def test_job_categories_invalid_token():
    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': 'invalid_token'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 401


def test_job_categories_expired_token():
    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': 'Bearer 6e81dcf8cd0f3651d393f712e6ee332b30a4ed2d'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 401
