from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.assertions.job_categories_assertions import assert_job_categories_created, assert_add_job_categories_schema
import json
from src.orangeHRM_api.api_requests import OrangeRequests
from conftest import post_teardown

def test_job_categories_success(test_login):
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
    # assert_add_job_categories_schema(response)
    assert response_data["name"] == job_category_name
    post_teardown(url, headers, response, "data")
    