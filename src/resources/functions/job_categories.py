from conftest import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests

def set_up_delete(login):
    url = f'{system_url}{Endpoints.job_categories.value}'
    headers = {'Authorization': f'{login}'}
    params = {'limit': 1, 'sortingFeild': 'id'}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    data = response_data["data"][0]
    return data