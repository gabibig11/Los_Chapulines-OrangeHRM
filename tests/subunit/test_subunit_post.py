import pytest
import requests
from config import system_url
from src.orangeHRM_api.api_requests import OrangeRequests
from src.assertions.subunit_assertions import *

def test_create_subunit_with_valid_data(test_login):
    token = test_login
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': token}
    data = {
        "unit_id": "D001",
        "name": "Orange Department D",
        "description": "",
        "parent_id": "1",
        "head_of_department_employee": "3"
    }
    response = OrangeRequests().post(url=url, headers=headers, data=data)  # Use 'json' parameter instead of 'data'
    assert_create_subunit_success(response)
def test_create_subunit_without_head_of_department(test_login):
    token = test_login
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': token}
    data = {
        "unit_id": "4",
        "name": "SubUnitC",
        "description": "test",
        "parent_id": "1",
        "cost_centre_id": "1"
    }
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    assert_create_subunit_success(response)


def test_create_subunit_with_invalid_access_token():
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': 'Bearer invalid_token'}
    data = {
        "unit_id": "4",
        "name": "SubUnitC",
        "description": "test",
        "parent_id": "1",
        "cost_centre_id": "1"
    }
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    assert_invalid_access_token(response)

def test_create_subunit_with_empty_access_token():
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': ''}
    data = {
        "unit_id": "4",
        "name": "SubUnitC",
        "description": "test",
        "parent_id": "1",
        "cost_centre_id": "1"
    }
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    assert_empty_access_token(response)

def test_create_subunit_with_unit_id_exceeding_limit(test_login):
    token = test_login
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': token}
    data = {
        "unit_id": "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890",  # Excede el límite de caracteres
        "name": "SubUnitC",
        "description": "test",
        "parent_id": "1",
        "cost_centre_id": "1"
    }
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    assert_unit_id_exceeds_limit(response)

def test_create_subunit_with_description_exceeding_limit(test_login):
    token = test_login
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': token}
    data = {
        "unit_id": "4",
        "name": "SubUnitC",
        "description": "a" * 401,  # Excede el límite de caracteres
        "parent_id": "1",
        "cost_centre_id": "1"
    }
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    assert_description_exceeds_limit(response)

def test_create_subunit_with_invalid_parent_id(test_login):
    token = test_login
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': token}
    data = {
        "unit_id": "4",
        "name": "SubUnitC",
        "description": "test",
        "parent_id": "invalid_parent_id",  # Parent ID inválido
        "cost_centre_id": "1"
    }
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    assert_invalid_parent_id(response)
