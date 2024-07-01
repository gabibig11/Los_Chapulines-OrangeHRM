from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.assertions.employment_status_assertions import assert_employment_status_schema, assert_employment_status_succesfuly
import pytest
import jsonschema
from src.orangeHRM_api.api_requests import OrangeRequests

@pytest.mark.smoke

def test_get_status_employe(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_employment_status_schema(response)

    #response_data = response.json()
    #assert response.status_code == 200
    #assert response_data['data'] is not None





