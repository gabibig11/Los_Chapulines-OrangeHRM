import requests
from tests.config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.utils.load_resources import load_schema_resource
import jsonschema


def test_job_categories_schema_file(test_login):
    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_data = response.json()

    schema = load_schema_resource("job_categories_schema.json")
    assert jsonschema.validate(instance=response_data, schema=schema) is None


def test_job_categories_success(test_login):
    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{test_login}'}
    response = requests.get(url, headers=headers)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['data'] is not None
