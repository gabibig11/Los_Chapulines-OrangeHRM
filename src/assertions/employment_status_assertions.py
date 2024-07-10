import pytest
import jsonschema
from src.utils.load_resources import load_schema_resource

def assert_employment_status_succesfuly(response):
    assert response.status_code == 200
    assert response.json()['data'] is not None

def assert_employment_status_created(response):
    assert response.status_code == 201
    assert response.json()['data'] is not None
def assert_employment_status_delete(response):
    assert response.status_code == 204


def assert_employment_status_schema(response):
    schema = load_schema_resource("job_categories_schema.json")
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")

def assert_employment_status_schema_post(payload):
    schema = load_schema_resource("employment_status_schema_add_input.json")
    try:
        jsonschema.validate(instance=payload, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        return False
        #pytest.fail(f'Se presento un error: {err}')
def assert_employment_schema_post_reponse(payload):
    schema = load_schema_resource("employment_status_schema_add.json")
    try:
        jsonschema.validate(instance=payload, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        return False

def assert_delete_employment_status_schema(payload):
    schema = load_schema_resource("job_categories_schema_delete.json")
    try:
        jsonschema.validate(instance=payload, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        return False
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")

def assert_get_employment_asc(response):
    response_json = response.json()
    response_data = response_json["data"]
    for i in range(len(response_data) - 1):
        current_id = int(response_data[i]["id"])
        next_id = int(response_data[i+1]["id"])
        assert current_id < next_id

def assert_get_employment_desc(response):
    response_json = response.json()
    response_data = response_json["data"]
    for i in range(len(response_data) - 1):
        current_id = int(response_data[i]["id"])
        next_id = int(response_data[i+1]["id"])
        assert current_id > next_id