import pytest
from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests
from src.assertions.nationality_assertions import AssertionNationality


@pytest.mark.smoke
#Verificar que la solicitud exitosa retorna un estado 200
def test_get_nationality_success(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    print(f'URL {url}')
    print(f'Token: {test_login}')
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    AssertionNationality.assert_status_code(response, 200)
    AssertionNationality.assert_nationality_list_schema(response.json())


#Verificar que la solicitud sin un token retorne un estado 401
def test_get_nationality_no_token():
    url = f'{system_url}{Endpoints.nationality_list.value}'
    print(f'URL {url}')
    headers = {}
    response = OrangeRequests().get(url, headers=headers)
    AssertionNationality.assert_status_code(response, 401)


#Verificar que la solicitud con un token inválido retorne un estado 401
def test_get_nationality_invalid_token():
    url = f'{system_url}{Endpoints.nationality_list.value}'
    print(f'URL {url}')
    headers = {'Authorization': 'Bearer INVALID_TOKEN'}
    response = OrangeRequests().get(url, headers=headers)
    AssertionNationality.assert_status_code(response, 401)

#Verificar que la solicitud con un token válido y parámetros válidos retorne un estado 200
def test_get_nationality_valid_token_and_parameters(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Authorization': test_login}
    params = {
        "limit": 10,
        "offset": 0,
        "sortingField": "name",
        "sortingOrder": "asc"
    }
    response = OrangeRequests().get(url, headers=headers, params=params)
    AssertionNationality.assert_status_code(response, 200)


#Verificar que la solicitud retorna la estructura JSON esperada
def test_nationality_json_structure(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Authorization': f'{test_login}'}
    orange_requests = OrangeRequests()
    response = orange_requests.get(url, headers=headers)
    AssertionNationality.assert_status_code(response, 200)
    AssertionNationality.assert_json_structure(response.json())


#Verificar que cada elemento en la lista data contiene las claves id y name
def test_get_nationality_data_keys(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Authorization': f'{test_login}'}
    orange_requests = OrangeRequests()
    response = orange_requests.get(url, headers=headers)
    AssertionNationality.assert_status_code(response, 200)
    AssertionNationality.assert_data_keys(response.json()['data'])


#Verificar que una solicitud con parámetros inválidos retorna un estado 400
def test_get_nationality_invalid_parameters():
    url = f'{system_url}{Endpoints.nationality_list.value}?invalid_param=value'
    orange_requests = OrangeRequests()
    response = orange_requests.get(url)
    AssertionNationality.assert_invalid_parameters(response)


#Verificar que la solicitud con el parámetro offset igual a 0 retorna la lista de equipos correctamente
def test_offset_zero_returns_correct_list(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}?offset=0'
    headers = {'Authorization': test_login}
    response = OrangeRequests().get(url, headers=headers)
    AssertionNationality.assert_status_code(response, 200)
    AssertionNationality.assert_correct_list(response.json())


#Verificar que la solicitud con el parámetro limit igual a 0 retorna una lista de equipos sin datos
def test_get_nationalities_limit_zero(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    print(f'URL {url}')
    print(f'Token: {test_login}')
    headers = {'Authorization': f'{test_login}'}
    params = {
        "limit": 0,
        "offset": 0,
        "sortingField": "name",
        "sortingOrder": "asc"
    }
    response = OrangeRequests().get(url, headers=headers, params=params)
    AssertionNationality.assert_status_code(response, 200)
    AssertionNationality.assert_limit_zero_response(response.json())


#Verificar que la solicitud no devuelva campos vacíos
def test_no_empty_fields_in_response(test_login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Authorization': f'{test_login}'}
    orange_requests = OrangeRequests()
    response = orange_requests.get(url, headers=headers)
    AssertionNationality.assert_status_code(response, 200)
    AssertionNationality.assert_no_empty_fields(response.json()['data'])