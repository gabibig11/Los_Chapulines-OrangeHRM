import json
import os
import jsonschema
import pytest
from src.utils.load_resources import load_schema_resource

def assert_create_subunit_success(response):
    assert response.status_code == 400

def assert_invalid_access_token(response):
    assert response.status_code == 401
def assert_empty_access_token(response):
    assert response.status_code == 401

def assert_empty_name(response):
    assert response.status_code == 400

def assert_unit_id_exceeds_limit(response):
    assert response.status_code == 400

def assert_description_exceeds_limit(response):
    assert response.status_code == 400

def assert_invalid_parent_id(response):
    assert response.status_code == 400

##########GET######33##

def  assert_subunit_valid(response):
    assert response.status_code == 200

def  assert_subunit_not_found(response):
    assert response.status_code == 200

def assert_subunit_list(response):
    assert response.status_code == 200

def assert_subunit_list_with_name_filter(response):
 assert response.status_code == 200

def assert_invalid_request(response):
    assert response.status_code == 400 or response.status_code == 200

def assert_subunit_list_with_cost_centre_id_filter(response):
    assert response.status_code == 200

def assert_list_sorted(response):
    assert response.status_code == 200