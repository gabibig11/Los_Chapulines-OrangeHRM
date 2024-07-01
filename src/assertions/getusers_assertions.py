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

def assert_getusers_filter_schema(response):
    filename = "getusers_filter_schema.json"
    schema = load_schema_resource(filename)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error de Schema {err}')

def assert_count_users(response, users_counted):
    count_response=len(response['data'])
    assert count_response==users_counted

"""def assert_getusers_filter_include_employee_schema(response):
    filename = "getusers_filter_include_employee_schema.json"
    schema = load_schema_resource(filename)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error de Schema {err}')"""

def assert_getusers_filter_coincidences(response, filter_value, atribute):
    users=response['data']
    for user in users:
        json_atribute = user[atribute]
        assert filter_value==json_atribute

def assert_getusers_filter_order_all_values(response, atribute):
    users=response['data']
    if atribute=='id' or atribute=='status':
        values = [int(user[atribute]) for user in users]
        assert values == sorted(values)
    else:
        values = [user[atribute] for user in users]
        assert values == sorted(values, key=lambda s: s.lower())

def assert_getusers_filter_include_schema(response):
    filename="getusers_filter_include_schema.json"
    schema=load_schema_resource(filename)
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error de Schema {err}')
