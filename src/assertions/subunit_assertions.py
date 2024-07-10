
import jsonschema
import pytest
from src.utils.load_resources import load_schema_resource



def assert_subunit_auth_error(response, n):
    if n == 1:
        assert response["error"] == "invalid_token"
        assert response["error_description"] == "The access token provided is invalid"
    elif n == 2:
        assert response["error"] == "expired_token"
        assert response["error_description"] == "The access token provided has expired"
    else:
        assert response["error"] == 'invalid_request'
        assert response["error_description"] == "Malformed auth header"

def assert_subunit_delete_schema(subunit_delete):
    schema = load_schema_resource("subunit_delete_schema.json")
    try:
        jsonschema.validate(instance=subunit_delete, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presentó un error: {err}')
