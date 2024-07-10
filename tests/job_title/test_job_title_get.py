
from conftest import *
from config import system_url, random_token, expired_token
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests
from src.assertions.job_title_assertions import assert_job_title_auth_error, assert_job_titles_schema

parametros = {'limit': 10, 'offset': 0, 'sortingField': 'id', 'sortingOrder': 'ASC'}


# Verificar respuesta exitosa al momento de obtener todos los cargos laborales
@pytest.mark.smoke
def test_job_title_success(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    response_data = response.json()
    assert assert_job_titles_schema(response_data) == True
    assert response.status_code == 200
    assert response_data['data'] is not None


# Verificar respuesta fallida sin token
def test_job_title_no_token():
    url = f'{system_url}{Endpoints.job_titles.value}'
    response = OrangeRequests().get(url)
    response_err = response.json()
    assert response.status_code == 401
    assert response_err == []


# Verificar respuesta fallida con un token inválido, expirado e incompleto
@pytest.mark.parametrize("wrong_token, case", [(f'Bearer {random_token}', 1),  # test_job_title_invalid_token
                                               (expired_token, 2),  #test_job_title_expired_token
                                               ("Bearer", 3)])  # test_job_title_incomplete_header
def test_job_title_no_authorization(wrong_token, case):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': f'{wrong_token}'}
    response = OrangeRequests().get(url, headers=headers)
    response_data = response.json()
    assert response.status_code == 401
    assert_job_title_auth_error(response_data, case)


# Verificar que la respuesta tengo el formato correcto
def test_schema_job(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': f'{test_login}'}
    params = parametros
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_schema = response.json()
    assert assert_job_titles_schema(response_schema) == True
    assert response.status_code == 200


# Verificar que los campos de respuesta no están vacíos al solicitar los cargos laborales
def test_job_title_not_empty_labels(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    response_data = response.json()
    assert assert_job_titles_schema(response_data) == True
    for job_title_object in response_data['data']:
        assert job_title_object['id'] is not None
        assert job_title_object['jobTitleName'] is not None
        assert job_title_object['jobDescription'] is not None
        assert job_title_object['note'] is not None
        assert job_title_object['isDeleted'] is not None


# Verificar respuesta  con parámetro sortingField
@pytest.mark.parametrize("case", ['id', 'jobTitleName', 'jobDescription'])
def test_job_title_sortingField(test_login, case):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': f'{test_login}'}
    params = {'sortingField': f'{case}'}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response_data['data'] is not None


# Verificar la combinación de parámetros limit y sortingField
@pytest.mark.parametrize("case", ['id', 'jobTitleName', 'jobDescription'])
def test_job_title_sortingField_limit(test_login, case):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': f'{test_login}'}
    params = {'limit': 10, 'sortingField': f'{case}'}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    cont = len(response_data['data'])
    assert response_data['data'] is not None
    assert cont == 10


# Verificar que el orden sea ascendente en la combinación de parámetros sortingField y sortingOrder
def test_job_title_sortingOrder_asc(test_login):  # consulta viene por defecto desc
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': f'{test_login}'}
    params = {'sortingField': 'id', 'sortingOrder': 'ASC'}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    data = response_data['data']
    asc = False
    for i in range(len(data) - 1):
        actual_id = int(data[i]['id'])
        next_id = int(data[i + 1]['id'])

        if actual_id <= next_id:
            asc = True
            break
    assert asc == True


# Verificar la combinación de todos los parámetros
def test_job_title_params(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': f'{test_login}'}
    params = parametros
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response_data['data'] is not None


# Verificar el manejo de parámetros inválidos
def test_job_title_invalid_params(test_login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': f'{test_login}'}
    params = {'limit': 10, 'offset': 0, 'sortingField': 'id', 'order': 'ASC'}  # order en vez de sortingOrder
    response = OrangeRequests().get(url, headers=headers, params=params)
    assert response.status_code == 400
