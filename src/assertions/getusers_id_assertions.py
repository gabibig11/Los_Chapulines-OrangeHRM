import pytest
import jsonschema
from src.utils.load_resources import load_schema_resource
def assert_getusers_id_schema(response):
    filename="getusers_id_oneuser_schema.json"
    schema=load_schema_resource(filename)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error de Schema {err}')

def assert_getusers_id_include_schema(response):
    filename="getusers_id_include_oneuser_schema.json"
    schema=load_schema_resource(filename)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error de Schema {err}')