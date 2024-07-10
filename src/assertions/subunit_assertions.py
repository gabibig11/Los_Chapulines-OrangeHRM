import json
import os
from jsonschema import validate

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

