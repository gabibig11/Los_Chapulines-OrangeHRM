from config import system_url, random_token, expired_token
from src.orangeHRM_api.endpoints import Endpoints
from src.assertions.job_categories_assertions import assert_job_categories_created, assert_add_job_categories_schema, assert_add_job_categries_schema_input
import json
from src.orangeHRM_api.api_requests import OrangeRequests
from conftest import post_teardown
import pytest

@pytest.mark.smoke
def test_job_categories_add_success(test_login):
    job_category_name = "Prueba Orange3"
    data = {
        "name" : job_category_name
    }

    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    assert assert_add_job_categries_schema_input(data) == True
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    assert_job_categories_created(response)
    assert_add_job_categories_schema(response)
    post_teardown(url=url, headers=headers, response=response.json(), attribute_search="id", attribute_delete="data", array=True)


def test_job_categories_add_name_already_exists(test_login):
    job_category_name = "Prueba Orange2"
    data = {
        "name" : job_category_name
    }

    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().post(url, headers=headers, data=data)
    assert response.status_code == 400


def test_job_categories_add_name_than_50_characters(test_login):
    job_category_name = "Este es un nombre muuuuuuuuuuuuuuuuuuuuuuy laaargoooooooo"
    data = {
        "name" : job_category_name
    }

    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().post(url, headers=headers, data=data)
    assert response.status_code == 500


@pytest.mark.xfail(reason="Crea una categoria de trabajo con solo dos caracteres-H201 Verificar que no se pueda agregar una categoría de trabajo con menos de dos caracteres en el name.")
def test_job_categories_add_name_less_than_2_characters(test_login):
    job_category_name = "as"
    data = {
        "name" : job_category_name
    }

    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().post(url, headers=headers, data=data)
    assert response.status_code == 500


def test_job_categories_add_empty_name(test_login):
    job_category_name = ""
    data = {
        "name" : job_category_name
    }

    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().post(url, headers=headers, data=data)
    assert response.status_code == 500


@pytest.mark.xfail(reason="Crea una categoria de trabajo con solo caracteres especiales-H201 Verificar que no se pueda agregar una categoría de trabajo con solo caracteres especiales en name")
def test_job_categories_add_name_only_special_characters(test_login):
    job_category_name = "++++"
    data = {
        "name" : job_category_name
    }

    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().post(url, headers=headers, data=data)
    assert response.status_code == 500


@pytest.mark.xfail(reason="Crea una categoria de trabajo con solo numeros en name-H201 Verificar que no se pueda agregar una categoría de trabajo con solo numeros en name")
def test_job_categories_add_name_only_numbers(test_login):
    job_category_name = "1234"
    data = {
        "name" : job_category_name
    }

    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().post(url, headers=headers, data=data)
    assert response.status_code == 500


def test_job_categories_add_invalid_token():
    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{random_token}'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 401


def test_job_categories_add_expired_token():
    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{expired_token}'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 401