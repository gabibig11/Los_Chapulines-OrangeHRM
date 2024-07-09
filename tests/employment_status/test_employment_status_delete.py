import pytest
from config import system_url, random_token, expired_token
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests
from src.assertions.employment_status_assertions import *

@pytest.mark.smoke
def test_employment_status_delete(test_login):

     data = {
         "name" : "Augusta"
     }

     url = f'{system_url}{Endpoints.employment_status.value}'
     headers = {'Authorization': f'{test_login}'}
     response = OrangeRequests().post(url=url, headers=headers, data=data)
     response_json = response.json()
     response_data = response_json["data"]
     created_id=response_data["id"]
     payload={"data" : [created_id]}
     response_delete = OrangeRequests().delete(url=url, headers=headers, data=payload)
     assert_employment_status_delete(response_delete)


#def test_employment_categories_delete_invalido(test_login):
 #         payload = {
  #             "data": ["id_invalido"]
   #       }
#
 #         url = f'{system_url}{Endpoints.employment_status.value}'
  #        headers = {'Authorization': f'{test_login}'}
   #       response = OrangeRequests().delete(url, headers=headers, data=payload)
    #      assert response.status_code == 400