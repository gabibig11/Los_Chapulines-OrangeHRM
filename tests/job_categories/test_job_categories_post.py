from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.assertions.job_categories_assertions import assert_job_categories_created, assert_add_job_categories_schema
import json
from src.orangeHRM_api.api_requests import OrangeRequests
from conftest import post_teardown
import pytest

def test_job_categories_add_success(test_login):
    job_category_name = "Prueba Orange3"
    data = {
        "name" : job_category_name
    }

    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    response = OrangeRequests().post(url, headers=headers, data=json.dumps(data))
    
    response_json = response.json()
    response_data = response_json["data"]

    assert_job_categories_created(response)
    assert_add_job_categories_schema(response)
    post_teardown(url, headers, response, "data")


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


@pytest.mark.xfail(reason="Crea una categoria de trabajo con solo dos caracteres-H202 Verificar que no se pueda agregar una categoría de trabajo con menos de dos caracteres en el name.")
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
    job_category_name = " "
    data = {
        "name" : job_category_name
    }

    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().post(url, headers=headers, data=data)
    assert response.status_code == 500


@pytest.mark.xfail(reason="Crea una categoria de trabajo con solo caracteres especiales-H202 Verificar que no se pueda agregar una categoría de trabajo con solo caracteres especiales en name")
def test_job_categories_add_name_only_special_characters(test_login):
    job_category_name = "++++"
    data = {
        "name" : job_category_name
    }

    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().post(url, headers=headers, data=data)
    assert response.status_code == 500