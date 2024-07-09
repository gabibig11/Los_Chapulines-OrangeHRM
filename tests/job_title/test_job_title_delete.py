
from config import random_token, expired_token
from conftest import *
from src.resources.functions.job_title import random_info, set_up_delete
from src.assertions.job_title_assertions import assert_job_title_delete_schema, assert_job_title_auth_error


# Verificar que se pueda eliminar un cargo laboral con parámetro id correcto
@pytest.mark.smoke
def test_job_title_delete_success(test_login):
    login = test_login
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{login}'}
    payload_id = set_up_delete(login=login)
    payload = {"data": [payload_id[0]]}
    print(payload)
    assert assert_job_title_delete_schema(payload) == True
    response = OrangeRequests().delete(url, headers=headers, data=payload)
    assert response.status_code == 204
    data = payload_id[1]
    print(data)
    delete_teardown(url, headers=headers, body=data)


# Verificar respuesta cuando se quiere eliminar un cargo con token inválido.
def test_job_title_delete_invalid_token():
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {random_token}'}
    response = OrangeRequests().delete(url, headers=headers)
    assert response.status_code == 401
    assert_job_title_auth_error(response.json(), 1)


# Verificar respuesta cuando se quiere eliminar un cargo con sesión expirada.
def test_job_title_delete_expired_token():
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': expired_token}
    response = OrangeRequests().delete(url, headers=headers)
    assert response.status_code == 401
    assert_job_title_auth_error(response.json(), 2)


# Verificar respuesta cuando se quiere eliminar un cargo sin token
def test_job_title_delete_without_token():
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json'}
    data = {"data": ["994"]}
    assert assert_job_title_delete_schema(data) == True
    response = OrangeRequests().delete(url, headers=headers, data=data)
    assert response.status_code == 401


# Verificar respuesta cuando se quiere hacer una petición con parámetro incorrecto
@pytest.mark.xfail(reason= "La petición muestra status 204 con body incorrecto-"
                           "H306-"
                           "Verificar respuesta cuando se quiere hacer una petición con body incorrecto")
def test_job_title_delete_incorrect_payload(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    data = {"id": [f'{random_info(4)}']}
    response = OrangeRequests().delete(url, headers=headers, data=data)
    assert response.status_code == 400


# Verificar respuesta cuando se quiere hacer una petición con body vacío
def test_job_title_delete_without_payload(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    response = OrangeRequests().delete(url, headers=headers)
    assert response.status_code == 400

# Verificar respuesta cuando se quiere eliminar un cargo con parámetro id incorrecto
def test_job_title_delete_invalid_id(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    data = {"data": [f'{random_info(4)}']}
    assert assert_job_title_delete_schema(data) == True
    response = OrangeRequests().delete(url, headers=headers, data=data)
    assert response.status_code == 400
