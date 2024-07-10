import pytest
from config import random_token, expired_token
from conftest import *
from src.assertions.nationality_assertions import (
    assert_nacionality_delete_schema,
    assert_nacionality_auth_error,
    assert_nationality_delete_schema
)
from src.resources.functions.nationality import set_up_delete
import json


@pytest.mark.smoke
def test_nationality_delete_success(test_login):
    login = test_login
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{login}'
    }
    payload_ids = set_up_delete(login=login)
    payload = {"data": payload_ids[0]}
    assert assert_nationality_delete_schema(payload)
    response = OrangeRequests().delete(url, headers=headers, data=json.dumps(payload))
    assert response.status_code == 204
    delete_teardown(url, headers=headers, body=payload_ids[1])


def test_nationality_delete_invalid_token():
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {random_token}'
    }
    response = OrangeRequests().delete(url, headers=headers)
    assert response.status_code == 401
    assert_nacionality_auth_error(response.json(), 1)


def test_nationality_delete_expired_token():
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': expired_token
    }
    response = OrangeRequests().delete(url, headers=headers)
    assert response.status_code == 401
    assert_nacionality_auth_error(response.json(), 2)


def test_nationality_delete_without_token():
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Content-Type': 'application/json'}
    payload = {"data": ["7", "6", "5"]}
    assert assert_nationality_delete_schema(payload)
    response = OrangeRequests().delete(url, headers=headers, data=json.dumps(payload))
    assert response.status_code == 401


@pytest.mark.xfail(reason="The request shows status 204 with incorrect body")
def test_nationality_delete_incorrect_payload(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{test_login}'
    }
    payload = {"id": ["1234"]}
    response = OrangeRequests().delete(url, headers=headers, data=json.dumps(payload))
    print(f"Response body: {response.text}")
    assert response.status_code == 400


def test_nationality_delete_response_structure(test_login):
    login = test_login
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{login}'
    }
    payload_ids = set_up_delete(login=login)
    payload = {"data": payload_ids[0]}
    response = OrangeRequests().delete(url, headers=headers, data=json.dumps(payload))
    assert response.status_code == 204

