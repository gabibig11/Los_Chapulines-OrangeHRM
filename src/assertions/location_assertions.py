import json

import pytest
import jsonschema
from src.utils.load_resources import load_schema_resource

def assert_location_schema(response):
    schema = load_schema_resource("location_schema_get.json")
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error: {err}')

def assert_location_schema_post(payload):
    schema = load_schema_resource("location_schema_post_input.json")
    try:
        jsonschema.validate(instance=payload, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        return False
        #pytest.fail(f'Se presento un error: {err}')
def assert_location_schema_post_reponse(payload):
    schema = load_schema_resource("location_schema_post_output.json")
    try:
        jsonschema.validate(instance=payload, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        return False
        #pytest.fail(f'Se presento un error: {err}')

def assert_location_schema_patch_success(payload):
    schema = load_schema_resource("location_schema_patch_success.json")
    try:
        jsonschema.validate(instance=payload, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        return False
        #pytest.fail(f'Se presento un error: {err}')
def assert_location_id_schema(response):
    schema = load_schema_resource("location_id_schema_get.json")
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'Se presento un error: {err}')

def assert_location_schema_delete_input(payload):
    schema = load_schema_resource("location_schema_delete_input.json")
    try:
        jsonschema.validate(instance=payload, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        return False

def assert_location_filter(response, filter, value_filter):
    for item in response["data"]:
        assert item[filter] == value_filter , 'El filtro no esta funcionando adecuadamente'


def assert_location_id(response, filter, value_filter):
    assert response["data"][filter] == value_filter

def assert_count_obj(response, count):
    actual_count = len(response["data"])
    assert actual_count == count, f'La cantidad de elementos que devolvio la consulta ({actual_count}) no es igual a {count} esperados'


def assert_data_empty(response):
    assert response["meta"]["total"] == 0

def assert_orderby_orderfilter(response, filter, orderby):
    values = [item[filter] for item in response['data'] if item[filter] is not None]
    values = [value.lower() for value in values]
    if orderby == "ASC":
        assert values == sorted(values), f'Los valores {filter} no estan ordenados de manera ASC'
    else :
        assert values == sorted(values, reverse=True), f'Los valores {filter} no estan ordenados de manera DESC'

def assert_orderby_orderfilter_id(response, orderby):
    values= [item["id"] for item in response['data']]
    values = [int(value) for value in values]

    if orderby == "ASC":
        assert values == sorted(values), f'Los valores {"id"} no estan ordenados de manera ASC'
    else:
        assert values == sorted(values, reverse=True), f'Los valores {"id"} no estan ordenados de manera DESC'

def assert_offset_orderby(response_orig, response_comp, offset):
    res_orig = json.loads(response_orig)
    res_comp = json.loads(response_comp)
    lista_ori=res_orig.get("data",[])
    lista_comp = res_comp.get("data",[])
    obj_ori= lista_ori[0]
    posicion = offset - 1
    obj_comp= lista_comp[posicion]
    print(obj_ori)
    print(obj_comp)
    assert obj_ori == obj_comp

