from typing import Dict

import requests

from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.assertions.employment_status_assertions import assert_employment_status_schema, \
    assert_employment_status_succesfuly
import pytest
import jsonschema
from src.orangeHRM_api.api_requests import OrangeRequests

@pytest.mark.smoke
def test_employment_status_token(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}'
    #print(url)
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    response_json = response.json()
    assert response.status_code == 200


def test_limit(test_login):
    limit = 2
    url = f'{system_url}{Endpoints.employment_status.value}?limit={limit}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    response_json = response.json()
    assert_employment_status_succesfuly(response)
    assert len(response_json['data']) == limit

def test_sortingOrder(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}?limit=10&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_data = response.json()

    assert response_data['data'] is not None

def test_sortingFeild(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}?limit=10&sortingFeild=id'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_data = response.json()
    assert response_data['data'] is not None

def test_limit_offset(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}?limit=10&offset=2'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_data = response.json()
    assert response_data['data'] is not None


def test_sortingFeild_sortingOrder(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}?sortingFeild=id&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_data = response.json()
    assert response_data['data'] is not None


def test_all(test_login):

    url = f'{system_url}{Endpoints.employment_status.value}?limit=4&offset=2&sortingFeild=id&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_data = response.json()
    assert response_data['data'] is not None


def test_expired_token():

    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Authorization': 'Bearer 6e81dcf8cd0f3651d393f712e6ee332b30a4ed2d'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 401


def test_invalid_token():
    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Authorization': 'invalid_token'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 401


def test_invalid_param(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}?invalidFilter=invalidFilterValue'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 400


def test_employment_status_schema(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_employment_status_schema(response)
