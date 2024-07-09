import json
import random
import string

import pytest

from config import random_token, expired_token
from conftest import *
from src.resources.functions.job_title import random_info
from src.assertions.job_title_assertions import assert_job_title_post_schema, assert_job_title_auth_error, \
    assert_job_title_post_response_schema, assert_job_title_labels_above_max_length

# Tomar en cuenta que el único label obligatorio es jobTitleName para crear un jobTitle

#Verificar que se pueda añadir un cargo laboral con todos los parámetros correctos. (**SMOKE**)
@pytest.mark.smoke
def test_job_title_post_sucess(test_login):
    url= f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    data = {
        "jobTitleName": "Respuesta de peticion automatizada sin []",
        "jobDescription": "Verificar la estructura de la respuesta y su status",
        "note": "Not null",
        "currentJobSpecification": "keepCurrent",
        "jobSpecification":
            {
                "base64": "ClVQREFURSBgb2hybV9tZW51X2l0ZW1gIFNFVCBg",
                "filename": "AccompanistAttachment.pdf",
                "filesize": "2000",
                "filetype": "application/pdf"
            }
    }
    assert assert_job_title_post_schema(data) == True
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    print(response.json())
    assert response.status_code == 201
    assert assert_job_title_post_response_schema(response.json()) == True
    post_teardown(url=url, headers=headers, response=response.json(), attribute_search="id", attribute_delete="data", array=True)


# Verificar respuesta cuando se quiere hacer una petición sin token
def test_job_title_post_no_token():
    url = f'{system_url}{Endpoints.job_titles.value}'
    payload = {
        "jobTitleName": "Respuesta de peticion automatizadaaa"
    }
    response = OrangeRequests().post(url=url, data=payload)
    response_err = response.json()
    assert response.status_code == 401
    assert response_err == []


# Verificar respuesta cuando se quiere añadir un cargo laboral con sesión expirada, invalida e incompleta
@pytest.mark.parametrize("wrong_token, case", [(f'Bearer {random_token}', 1),  # test_job_title_invalid_token
                                               (expired_token, 2),  #test_job_title_expired_token
                                               ("Bearer", 3)])  # test_job_title_incomplete_header
def test_job_title_post_no_authorization(wrong_token, case):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': wrong_token}
    payload = {"jobTitleName": "Respuesta de peticion automatizadaaa"}
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 401
    assert_job_title_auth_error(response_data, case)


# Verificar status con body vacío
def test_job_title_post_empty_payload(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().post(url=url, headers=headers)
    assert response.status_code == 500

# Verificar status cuando se quiere añadir un cargo laboral sin declarar 'jobTitleName'
def test_job_title_post_no_jobTitleName_label(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "jobDescription": "Verificar la estructura de la respuesta y su status",
        "note": "Not null"
    }
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 500


# Verificar status cuando se quiere añadir un cargo laboral sin data en campo jobTitleName.
def test_job_title_post_no_jobTitleName_data(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {"jobTitleName": ""}
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 400
    assert_job_title_labels_above_max_length(response_data)
    assert response_data["details"] == "jobTitleName [Required.]"


# Verificar respuesta cuando se excede límite de caracteres en jobTitleName.
def test_job_tile_post_jobTitleName_above_max_length(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "jobTitleName": f'{random_info(101)}'}
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 400
    assert_job_title_labels_above_max_length(response_data)


# Verificar respuesta cuando se excede límite de caracteres en jobDescription.
def test_job_tile_post_jobDescription_above_max_length(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "jobTitleName": "Respuesta de peticion automatizada",
        "jobDescription": random_info(401)
    }
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 400
    assert_job_title_labels_above_max_length(response_data)


# Verificar respuesta cuando se excede límite de caracteres en note.
def test_job_tile_post_note_above_max_length(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "jobTitleName": "Respuesta de peticion automatizada",
        "note": random_info(401)
    }
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 400
    assert_job_title_labels_above_max_length(response_data)


# Verificar que la solicitud POST con un filetype no soportado devuelve un error.
def test_job_tile_post_filetype_not_allowed(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "jobTitleName": "Respuesta de peticion automatizada",
        "jobSpecification":
            {
                "base64": "ClVQREFURSBgb2hybV9tZW51X2l0ZW1gIFNFVCBg",
                "filename": "AccompanistAttachment.pdf",
                "filesize": "2000",
                "filetype": "application/csv"
            }
    }
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 400
    assert response_data["title"] == "unsupported resource request"
    assert response_data["details"] == "filetype [unsupported resource request]"


# Verificar que la solicitud POST con un archivo que excede el tamaño permitido devuelve un error.
def test_job_tile_post_filesize_above_max_size(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "jobTitleName": "Respuesta de peticion automatizada",
        "jobSpecification":
            {
                "base64": "ClVQREFURSBgb2hybV9tZW51X2l0ZW1gIFNFVCBg",
                "filename": "AccompanistAttachment.pdf",
                "filesize": "5120000",
                "filetype": "application/csv"
            }
    }
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400

# Verificar respuesta declarando currentJobSpecification con los valores permitidos
# (replaceCurrent, deleteCurrent, keepCurrent, newAttachment).
@pytest.mark.parametrize("currentJobSpecification", ["replaceCurrent", "deleteCurrent", "keepCurrent", "newAttachment"])
def test_job_tile_post_allowed_currentJobSpecification_values(test_login, currentJobSpecification):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    data = {
        "jobTitleName": "Respuesta de peticion automatizada",
        "jobDescription": "Verificar la estructura de la respuesta y su status",
        "note": "Not null",
        "currentJobSpecification": currentJobSpecification,
        "jobSpecification":
            {
                "base64": "ClVQREFURSBgb2hybV9tZW51X2l0ZW1gIFNFVCBg",
                "filename": "AccompanistAttachment.pdf",
                "filesize": "1000",
                "filetype": "application/pdf"
            }
    }
    assert assert_job_title_post_schema(data) == True
    response = OrangeRequests().post(url=url, headers=headers, data=data)
    print(response.json())
    assert response.status_code == 201
    assert assert_job_title_post_response_schema(response.json()) == True
    post_teardown(url=url, headers=headers, response=response.json(), attribute_search="id", attribute_delete="data", array=True)


# Verificar respuesta con un valor no permitido en currentJobSpecification.
@pytest.mark.xfail(reason= "Se crea un cargo con valor no predeterminado encurrentJobSpecification -H302- Verificar respuesta con un valor no permitido en currentJobSpecificatio")
def test_job_tile_post_invalid_currentJobSpecification_value(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "jobTitleName": "Respuesta de peticion automatizada",
        "currentJobSpecification": f"{random_info(14)}"
    }
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400
