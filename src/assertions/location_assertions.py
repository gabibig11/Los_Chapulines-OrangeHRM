import pytest
import jsonschema
from src.utils.load_resources import load_schema_resource

def assert_location_schema(response):
    schema = load_schema_resource("location_schema.json")
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error: {err}')

def assert_location_id_schema(response):
    schema = load_schema_resource("location_id_schema.json")
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error: {err}')