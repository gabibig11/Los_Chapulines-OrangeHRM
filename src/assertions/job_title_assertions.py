import jsonschema
import pytest

from src.utils.load_resources import load_schema_resource


def assert_job_title_auth_error(response, n):
    if n == 1:
        assert response["error"] == "invalid_token"
        assert response["error_description"] == "The access token provided is invalid"
    elif n == 2:
        assert response["error"] == "expired_token"
        assert response["error_description"] == "The access token provided has expired"
    else:
        assert response["error"] == 'invalid_request'
        assert response["error_description"] == "Malformed auth header"


def assert_job_titles_schema(test_login_success):
    schema = load_schema_resource("job_titles_schema.json")
    try:
        jsonschema.validate(instance=test_login_success, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error: {err}')


def assert_job_title_post_schema(job_title_post):
    schema = load_schema_resource("job_title_post_schema.json")
    try:
        jsonschema.validate(instance=job_title_post, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error: {err}')


def assert_job_title_delete_schema(job_title_delete):
    schema = load_schema_resource("job_title_delete_schema.json")
    try:
        jsonschema.validate(instance=job_title_delete, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error: {err}')
