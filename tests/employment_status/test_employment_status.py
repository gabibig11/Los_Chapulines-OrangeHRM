from typing import Dict

import requests

from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.assertions.employment_status_assertions import assert_employment_status_schema, \
    assert_employment_status_succesfuly
import pytest
import jsonschema
from src.orangeHRM_api.api_requests import OrangeRequests
@pytest.mark.smoke
@pytest.mark.funtional
def test_employment_status_token(test_login):
    url = f'{system_url}{Endpoints.employment_status.value}'
    #print(url)
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    response_json = response.json()
    assert response.status_code == 200
@pytest.mark.funtional


