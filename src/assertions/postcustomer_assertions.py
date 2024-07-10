import pytest
import jsonschema
from src.utils.load_resources import load_schema_resource



def assert_postcustomer_schema(response):
    filename = "postcustomer_schema.json"
    schema = load_schema_resource(filename)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error de Schema {err}')
def assert_postcustomer_payload_schema(response):
    filename = "postcustomer_payload_schema.json"
    schema = load_schema_resource(filename)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error de Schema {err}')
