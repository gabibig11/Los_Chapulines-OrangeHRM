import json
import pytest

from conftest import *
from src.assertions.location_assertions import *

@pytest.mark.smoke()
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


def test_post_location_without_name(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = json.dumps({
        "city": "Cercado",
        "phone": "12345",
        "time_zone": "Pacific/Midway",
        "province": "Province of the location",
        "state": "State of the location",
        "address": "test",
        "zipCode": "12345",
        "fax": "12345",
        "notes": "test",
        "countryCode": "AU",
        "eeo_applicable": 0
    })
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400

def test_post_location_without_countryCode(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = json.dumps({
        "name": "gabibi.com",
        "city": "Cercado",
        "phone": "12345",
        "time_zone": "Pacific/Midway",
        "province": "Province of the location",
        "state": "State of the location",
        "address": "test",
        "zipCode": "12345",
        "fax": "12345",
        "notes": "test",
        "eeo_applicable": 0
    })
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_post_location_without_city(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = json.dumps({
        "name": "gabibi.com",
        "phone": "12345",
        "time_zone": "Pacific/Midway",
        "province": "Province of the location",
        "state": "State of the location",
        "address": "test",
        "zipCode": "12345",
        "fax": "12345",
        "notes": "test",
        "countryCode": "AU",
        "eeo_applicable": 0
    })
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400

def test_post_location_without_zipCode(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = json.dumps({
        "name": "gabibi.com",
        "city": "Cercado",
        "phone": "12345",
        "time_zone": "Pacific/Midway",
        "province": "Province of the location",
        "state": "State of the location",
        "address": "test",
        "fax": "12345",
        "notes": "test",
        "countryCode": "AU",
        "eeo_applicable": 0
    })
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400

def test_post_location_without_timezone(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = json.dumps({
        "name": "gabibi.com",
        "city": "Cercado",
        "phone": "12345",
        "province": "Province of the location",
        "state": "State of the location",
        "address": "test",
        "zipCode": "12345",
        "fax": "12345",
        "notes": "test",
        "countryCode": "AU",
        "eeo_applicable": 0
    })
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400

def test_post_location_invented_timezone(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = json.dumps({
        "name": "gabibi.com",
        "city": "Cercado",
        "phone": "12345",
        "time_zone": "La Paz/Bolivia",
        "province": "Province of the location",
        "state": "State of the location",
        "address": "test",
        "zipCode": "12345",
        "fax": "12345",
        "notes": "test",
        "countryCode": "AU",
        "eeo_applicable": 0
    })
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400

def test_location_post_maximum_exceed(test_login):
        url = f'{system_url}{Endpoints.location.value}'
        headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
        payload = json.dumps({
            "name": "cieeeeeeeeeeeeeeencaraaaaaaactersssssssssssssssssssnombreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            "city": "ciuuuuuuuuuudaaaaaaaaaaddddddddddgraaaaaaaaaaandee",
            "phone": "400 300 800 444 700 200 100 500",
            "time_zone": "Pacific/Midway",
            "province": "prooooooooviiiiiinciiiiiiiaaaaaamuyyyyyyylargaaaaaa",
            "state": "Caaaaalleeeeee waaaaaaalaaabeeee 402 Siiiidneeeyyyy",
            "address": "Cccccccccaaaaaaaaaaaaaalleeeeeeeeeeeee waaaaaaalaaaaaaaaaaabbbbbbbbeeeeeeeeeeeeeeeee 402 Siiiiiiiiiiiiiiiiiiiidneeeeeeeeeeeeeeeyyyyyyyyyyeeeeeeeeeeeeeeeeeeeeeeeeesquuuuuuuuuuuuuuiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiinaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 305",
            "zipCode": "400 300 800 444 700 200 100 500",
            "fax": "400 300 800 444 700 200 100 500",
            "notes": "test",
            "countryCode": "AU",
            "eeo_applicable": 0
        })
        response = OrangeRequests().post(url=url, headers=headers, data=payload)
        assert response.status_code == 400


def test_location_post_limit_maximum(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = json.dumps({
        "name": "cieeeeeeeeeeeeeencaraaaaaaactersssssssssssssssssssnombreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
        "city": "ciuuuuuuuuudaaaaaaaaaaddddddddddgraaaaaaaaaaandee",
        "phone": "40 300 800 444 700 200 100 500",
        "time_zone": "Pacific/Midway",
        "province": "proooooooviiiiiinciiiiiiiaaaaaamuyyyyyyylargaaaaaa",
        "state": "Caaaalleeeeee waaaaaaalaaabeeee 402 Siiiidneeeyyyy",
        "address": "Ccccccccaaaaaaaaaaaaaalleeeeeeeeeeeee waaaaaaalaaaaaaaaaaabbbbbbbbeeeeeeeeeeeeeeeee 402 Siiiiiiiiiiiiiiiiiiiidneeeeeeeeeeeeeeeyyyyyyyyyyeeeeeeeeeeeeeeeeeeeeeeeeesquuuuuuuuuuuuuuiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiinaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 305",
        "zipCode": "40 300 800 444 700 200 100 500",
        "fax": "40 300 800 444 700 200 100 500",
        "notes": "test",
        "countryCode": "AU",
        "eeo_applicable": 0
    })
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 201
    post_teardown(url=url, headers=headers, response=response, attribute="data")