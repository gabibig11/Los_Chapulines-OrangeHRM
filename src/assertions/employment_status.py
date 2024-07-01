import pytest
import jsonschema
from src.utils.load_resources import load_schema_resource

def assert_employment_satatus_schema(response):
    assert response.status_code == 200
    assert response.json()['data'] is not None


def assert_employment_satatus_schema(response):
    schema = load_schema_resource("job_categories_schema.json")
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")