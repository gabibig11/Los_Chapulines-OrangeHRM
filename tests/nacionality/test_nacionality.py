from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import Orange_requests
from src.assertions.nacionality_assertions import Assertion_nationality


#Verificar que la solicitud exitosa retorna un estado 200
def test_get_nationality_success(test_login):
    url = f'{system_url}{Endpoints.nacionality_list.value}'
    print(f'URL utilization: {url}')
    print(f'Token: {test_login}')
    headers = {'Authorization': f'{test_login}'}
    response = Orange_requests().get(url, headers=headers)
    Assertion_nationality.assert_status_code(response, 200)
    Assertion_nationality.assert_nationality_list_schema(response.json())


#Verificar que la solicitud sin un token retorne un estado 401
def test_get_nationality_without_token():
    url = f'{system_url}{Endpoints.nacionality_list.value}'
    print(f'URL utilization: {url}')
    headers = {}
    response = Orange_requests().get(url, headers=headers)
    Assertion_nationality.assert_status_code(response, 401)


#Verificar que la solicitud con un token inválido retorne un estado 401
def test_get_nationality_with_invalid_token():
    url = f'{system_url}{Endpoints.nacionality_list.value}'
    print(f'URL utilization: {url}')
    headers = {'Authorization': 'Bearer invalid_token'}
    response = Orange_requests().get(url, headers=headers)
    Assertion_nationality.assert_status_code(response, 401)
