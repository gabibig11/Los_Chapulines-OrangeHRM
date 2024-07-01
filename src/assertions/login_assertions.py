import pytest
import jsonschema
#from utilds
from src.utils.load_resources import load_schema_resource

from src.utils.load_resources import load_schema_resource


def assert_login_success(test_login_success):
    assert test_login_success["token_type"] is not None
    assert test_login_success["access_token"] is not None


def assert_login_failed(response):
    assert response["error"] == "invalid_request"
    assert response["error_description"] == "The grant type was not specified in the request"


def assert_login_blocked(response):
    assert response["error"] == "temporarily_blocked"
    assert response["error_description"] == "You have been restricted from accessing OrangeHRM temporarily."


def assert_login_schema(test_login_success):
    schema = load_schema_resource("login_schema.json")
    try:
        jsonschema.validate(instance=test_login_success, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error: {err}')
