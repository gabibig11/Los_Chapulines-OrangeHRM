import pytest
import jsonschema
from src.utils.load_resources import load_schema_resource


def assert_postvacancy_schema(response):
    filename = "postvacancy_schema.json"
    schema = load_schema_resource(filename)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error de Schema {err}')

def assert_postvacancy_error_400_schema(response):
    filename = "postvacancy_error_400_schema.json"
    schema = load_schema_resource(filename)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error de Schema {err}')

def assert_postvacancy_payload_schema(response):
    filename = "postvacancy_payload_schema.json"
    schema = load_schema_resource(filename)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error de Schema {err}')