import json
import jsonschema
import pytest
from src.utils.load_resources import load_schema_resource


def assert_nationality_list_schema(response):
    schema = load_schema_resource("nationality_schema.json")
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema don't match: {err}")


def assert_expired_token(response, response_err):
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    assert response_err['error'] == "expired_token", f"Expected 'expired_token' error, but got {response_err.get('error')}"
    assert response_err['error_description'] == "The access token provided has expired", f"Expected error description 'The access token provided has expired', but got {response_err.get('error_description')}"


def assert_invalid_token(response, response_err):
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    if not response_err:
        pytest.fail("Expected error response, but got an empty response")
    elif isinstance(response_err, dict):
        assert response_err.get(
            'error') == "invalid_token", f"Expected 'invalid_token' error, but got {response_err.get('error')}"
        assert response_err.get(
            'error_description') == "The access token provided is invalid", f"Expected error description 'The access token provided is invalid', but got {response_err.get('error_description')}"
    else:
        pytest.fail(f"Expected error response to be a dict, but got {type(response_err).__name__}")


def assert_json_structure(response_json):
    assert 'data' in response_json or 'errors' in response_json, "Key 'data' or 'errors' is not present in the JSON response"


def assert_data_keys(data):
    for item in data:
        assert 'id' in item, "Key 'id' is not present in one of the data elements"
        assert 'name' in item, "Key 'name' is not present in one of the data elements"


def assert_invalid_parameters(response):
    assert response.status_code in [400, 401, 500], \
        f"Expected status code 400, 401, or 500 for invalid parameters, got {response.status_code}"


def assert_correct_list(response_json):
    assert 'data' in response_json, "Key 'data' is missing in response"
    assert len(response_json['data']) > 0, "Expected non-empty list of data"


def assert_empty_list(response_json):
    assert 'data' in response_json, "Key 'data' is missing in response"
    assert len(response_json['data']) == 0, "Expected empty list, but received data"


def assert_limit_zero_response(response_json):
    assert "data" in response_json, "The response does not contain the 'data' field"
    assert isinstance(response_json["data"], list), "The 'data' field is not a list"
    if len(response_json["data"]) > 0:
        print("Warning: The parameter limit=0 is not working as expected. The nationalities list is not empty.")
    else:
        assert len(response_json["data"]) == 0


def assert_no_empty_fields(data):
    for item in data:
        for key, value in item.items():
            assert value is not None and value != '', f"Field '{key}' in item {item} is empty or None"


def assert_nationality_post_schema(nationality_post_schema):
    schema = load_schema_resource("nationality_post_schema.json")
    try:
        jsonschema.validate(instance=nationality_post_schema, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'error: {err}')

def assert_nationality_post_schema_response(payload):
    schema = load_schema_resource("nationality_post_response_schema.json")
    try:
        jsonschema.validate(instance=payload, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        return False


