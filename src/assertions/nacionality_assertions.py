import jsonschema
import pytest
from src.utils.load_resources import load_schema_resource
from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import Orange_requests

class Assertion_nationality:
    @staticmethod
    def assert_status_code(response, expected_status_code):
        assert response.status_code == expected_status_code


    def assert_nationality_list_schema(response):
         schema = load_schema_resource("nacionality_schema.json")
         try:
             jsonschema.validate(instance=response, schema=schema)
             return True
         except jsonschema.exceptions.ValidationError as err:
            pytest.fail(f"JSON schema dont match {err}")

    def test_get_nationality_success(test_login):
         url = f'{system_url}{Endpoints.nacionality_list.value}'
         print(f'URL utilization: {url}')
         print(f'Token: {test_login}')
         headers = {'Authorization': f'{test_login}'}
         response = Orange_requests().get(url, headers=headers)
         Assertion_nationality.assert_status_code(response, 200)
         Assertion_nationality.assert_nationality_list_schema(response.json())

    def test_get_nationality_without_token(self):
         url = f'{system_url}{Endpoints.nacionality_list.value}'
         print(f'URL utilization: {url}')
         headers = {}
         response = Orange_requests().get(url, headers=headers)
         Assertion_nationality.assert_status_code(response, 401)

    def test_get_nationality_with_invalid_token(self):
        url = f'{system_url}{Endpoints.nacionality_list.value}'
        print(f'URL utilization: {url}')
        headers = {'Authorization': 'Bearer INVALID_TOKEN'}
        response = Orange_requests().get(url, headers=headers)
        Assertion_nationality.assert_status_code(response, 401)
