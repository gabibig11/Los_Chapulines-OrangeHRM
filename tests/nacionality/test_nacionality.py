
from config import system_url
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests
from src.assertions.nacionality_assertions import AssertionNationality
from src.assertions.nacionality_schema_assertions import AssertionSchemaNationality

def test_get_nationality_success(test_login):
    url = f'{system_url}{Endpoints.nacionality_list.value}'
    print(f'URL utilizada: {url}')
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    AssertionNationality.assert_status_code(response, 200)
    AssertionSchemaNationality.assert_nationality_list_schema(response.json())
