import pytest
import requests
from config import system_url
from src.orangeHRM_api.api_requests import OrangeRequests
from src.assertions.subunit_assertions import *

def test_get_subunit_valid_id(test_login):
    token = test_login
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': token}
    params = {
        "unit_id": "D001"
    }
    response = OrangeRequests().get(url=url, headers=headers, params=params)
    assert_subunit_valid(response)

def test_get_subunit_invalid_token():
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': 'Bearer invalid_token'}
    params = {
        "unit_id": "1"
    }
    response = OrangeRequests().get(url=url, headers=headers, params=params)
    assert_invalid_access_token(response)

def test_get_subunit_not_found(test_login):
    token = test_login
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': token}
    params = {
        "unit_id": "D0004"
    }
    response = OrangeRequests().get(url=url, headers=headers, params=params)
    assert_subunit_not_found(response)

def test_get_subunits_list(test_login):
    token = test_login
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': token}
    response = OrangeRequests().get(url=url, headers=headers)
    assert_subunit_list(response)

def test_get_subunits_with_name_filter(test_login):
    token = test_login
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': token}
    params = {
        "fields[]": "name"
    }
    response = OrangeRequests().get(url=url, headers=headers, params=params)
    assert_subunit_list_with_name_filter(response)

def test_get_subunits_with_cost_centre_id_filter(test_login):
    token = test_login
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': token}
    params = {
        "fields[]": "cost_centre_id"
    }
    response = OrangeRequests().get(url=url, headers=headers, params=params)
    assert_subunit_list_with_cost_centre_id_filter(response)

def test_get_subunits_sorted_asc(test_login):
    token = test_login
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': token}
    params = {
        "sortingOrder": "ASC"
    }
    response = OrangeRequests().get(url=url, headers=headers, params=params)
    assert_list_sorted(response)

def test_get_subunits_sorted_desc(test_login):
    token = test_login
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': token}
    params = {
        "sortingOrder": "DESC"
    }
    response = OrangeRequests().get(url=url, headers=headers, params=params)
    assert_list_sorted(response)

def test_get_subunits_invalid_request(test_login):
    token = test_login
    url = f"{system_url}/api/subunits"
    headers = {'Authorization': token}
    params = {
        "invalid_param": "true"
    }
    response = OrangeRequests().get(url=url, headers=headers, params=params)
    assert_invalid_request(response)
