import jsonschema
import pytest

from src.utils.load_resources import load_schema_resource


def assert_get_job_categories_succesfuly(response):
    assert response.status_code == 200
    assert response.json()['data'] is not None


def assert_job_categories_created(response):
    assert response.status_code == 201
    assert response.json()['data'] is not None


def assert_job_categories_delete(response):
    assert response.status_code == 204


def assert_get_job_categories_schema(response):
    schema = load_schema_resource("job_categories_schema.json")
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")


def assert_add_job_categories_schema(response):
    schema = load_schema_resource("job_categories_schema_add.json")
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")


def assert_add_job_categries_schema_input(payload):
    schema = load_schema_resource("job_categories_schema_add_input.json")
    try:
        jsonschema.validate(instance=payload, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        return False
    

def assert_delete_job_categories_schema(payload):
    schema = load_schema_resource("job_categories_schema_delete.json")
    try:
        jsonschema.validate(instance=payload, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        return False
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")