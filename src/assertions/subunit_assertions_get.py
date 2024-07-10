import jsonschema
import pytest
from src.utils.load_resources import load_schema_resource


def assert_subunit_schema(response):
    schema = load_schema_resource("subunit_schema_get.json")
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema don't match: {err}")


def assert_subunit_list_schema(response):
    schema = load_schema_resource("subunit_list_schema_get.json")
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema don't match: {err}")


def assert_subunit_not_found(response):
    assert response["message"] == "Subunit not found"


def assert_subunit_list_sorted(response, sorting_order):
    if sorting_order == "ASC":
        # Implement assertion for ascending order
        pass
    elif sorting_order == "DESC":
        # Implement assertion for descending order
        pass
    else:
        pytest.fail("Invalid sorting order specified")


def assert_subunit_invalid_request(response):
    assert response["error"] == "invalid_request"
    assert "error_description" in response


def assert_subunit_auth_error(response, expected_error):
    assert response["error"] == expected_error["error"]
    assert response["error_description"] == expected_error["error_description"]
