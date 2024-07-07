import json

import pytest

from conftest import *
from src.assertions.location_assertions import *

def test_location_post_sucess(test_login):
    url= f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload= json.dumps({
              "name":"gabibi.com",
              "city":"Cercado",
              "phone":"12345",
              "time_zone":"Pacific/Midway",
              "province":"Province of the location",
              "state":"State of the location",
              "address":"test",
              "zipCode":"12345",
              "fax":"12345",
              "notes":"test",
              "countryCode":"AU",
              "eeo_applicable": 0
            })
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code ==201


    post_teardown(url=url, headers=headers, response=response, attribute="data")





