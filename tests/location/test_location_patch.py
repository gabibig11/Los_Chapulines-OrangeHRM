from config import *
from conftest import *
from src.assertions.location_assertions import *
from src.orangeHRM_api.api_requests import OrangeRequests

@pytest.mark.smoke
def test_location_patch_success(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
              "name":"pruebas_patch.com",
              "city":"Diplomado/San Simon",
              "phone":"12345678",
              "time_zone":"Pacific/Midway",
              "province":"FCyt",
              "state":"State of the location",
              "address":"Oquendo",
              "zipCode":"12345678",
              "fax":"12345678",
              "notes":"test_success",
              "countryCode":"AU",
              "eeo_applicable": 0
            }
    assert assert_location_schema_post(payload) == True
    response = OrangeRequests().patch(url=url, headers=headers, data=payload )
    assert response.status_code == 200
    assert assert_location_schema_patch_success(response.json()) == True


def test_patch_location_without_name(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
              "name": None,
              "city":"Diplomado/San Simon",
              "phone":"12345678",
              "time_zone":"Pacific/Midway",
              "province":"FCyt",
              "state":"State of the location",
              "address":"Oquendo",
              "zipCode":"12345678",
              "fax":"12345678",
              "notes":"test_success",
              "countryCode":"AU",
              "eeo_applicable": 0
    }
    assert assert_location_schema_post(payload) == False
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_patch_location_without_countryCode(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "name": "pruebas_patch.com",
        "city": "Diplomado/San Simon",
        "phone": "12345678",
        "time_zone": "Pacific/Midway",
        "province": "FCyt",
        "state": "State of the location",
        "address": "Oquendo",
        "zipCode": "12345678",
        "fax": "12345678",
        "notes": "test_success",
        "countryCode": None,
        "eeo_applicable": 0
    }
    assert assert_location_schema_post(payload) == False
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 400

def test_patch_location_without_city(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
              "name":"pruebas_patch.com",
              "city":None,
              "phone":"12345678",
              "time_zone":"Pacific/Midway",
              "province":"FCyt",
              "state":"State of the location",
              "address":"Oquendo",
              "zipCode":"12345678",
              "fax":"12345678",
              "notes":"test_success",
              "countryCode":"AU",
              "eeo_applicable": 0
            }
    assert assert_location_schema_post(payload) == False
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_patch_location_without_zipCode(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
              "name":"pruebas_patch.com",
              "city":"Diplomado/San Simon",
              "phone":"12345678",
              "time_zone":"Pacific/Midway",
              "province":"FCyt",
              "state":"State of the location",
              "address":"Oquendo",
              "zipCode":None,
              "fax":"12345678",
              "notes":"test_success",
              "countryCode":"AU",
              "eeo_applicable": 0
            }
    assert assert_location_schema_post(payload) == False
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 400

@pytest.mark.xfail (reason= "Error al mandar actualizacion de locacion sin timezone H403-Verificar que no se permita actualiza una locacion sin timezone" )
def test_patch_location_without_timezone(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
              "name":"pruebas_patch.com",
              "city":"Diplomado/San Simon",
              "phone":"12345678",
              "time_zone": None,
              "province":"FCyt",
              "state":"State of the location",
              "address":"Oquendo",
              "zipCode":"12345678",
              "fax":"12345678",
              "notes":"test_success",
              "countryCode":"AU",
              "eeo_applicable": 0
            }
    assert assert_location_schema_post(payload) == False
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_patch_location_invented_timezone(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
              "name":"pruebas_patch.com",
              "city":"Diplomado/San Simon",
              "phone":"12345678",
              "time_zone":"Piplomado/San Simon",
              "province":"FCyt",
              "state":"State of the location",
              "address":"Oquendo",
              "zipCode":"12345678",
              "fax":"12345678",
              "notes":"test_success",
              "countryCode":"AU",
              "eeo_applicable": 0
            }
    assert assert_location_schema_post(payload) == True
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_location_patch_maximum_exceed(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
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
    }
    assert assert_location_schema_post(payload) == True
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_location_patch_limit_maximum(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "name": "cieeeeeeeeeeeencaraaaaaaactersssssssssssssssssssnombreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
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
    }
    assert assert_location_schema_post(payload) == True
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 200
    assert assert_location_schema_patch_success(response.json()) == True


def test_location_patch_without_field_non_mandatory(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "name": "pruebas_patch.com",
        "city": "Diplomado/San Simon",
        "phone": "12345678",
        "time_zone": "Pacific/Midway",
        "province": "FCyt",
        "state": "State of the location",
        "address": "Oquendo",
        "zipCode": "12345678",
        "fax": None,
        "notes": "test_success",
        "countryCode": "AU",
        "eeo_applicable": 0
    }
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 200
    assert assert_location_schema_patch_success(response.json()) == True


def test_location_patch_field_invented(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "name": "pruebas_patch.com",
        "city": "Diplomado/San Simon",
        "phone": "12345678",
        "time_zone": "Pacific/Midway",
        "province": "FCyt",
        "state": "State of the location",
        "address": "Oquendo",
        "zipCode": "12345678",
        "fax": "12345678",
        "notes": "test_success",
        "countryCode": "AU",
        "emergency_contact": "444 601 305 08",
        "eeo_applicable": 0
    }
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_location_patch_token_invented(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{random_token}'}
    payload = {
        "name": "pruebas_patch.com",
        "city": "Diplomado/San Simon",
        "phone": "12345678",
        "time_zone": "Pacific/Midway",
        "province": "FCyt",
        "state": "State of the location",
        "address": "Oquendo",
        "zipCode": "12345678",
        "fax": "12345678",
        "notes": "test_success",
        "countryCode": "AU",
        "eeo_applicable": 0
    }

    assert assert_location_schema_post(payload) == True
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 401


def test_location_patch_token_expired(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{expired_token}'}
    payload = {
        "name": "pruebas_patch.com",
        "city": "Diplomado/San Simon",
        "phone": "12345678",
        "time_zone": "Pacific/Midway",
        "province": "FCyt",
        "state": "State of the location",
        "address": "Oquendo",
        "zipCode": "12345678",
        "fax": "12345678",
        "notes": "test_success",
        "countryCode": "AU",
        "eeo_applicable": 0
    }

    assert assert_location_schema_post(payload) == True
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 401


def test_location_patch_without_token(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json'}
    payload = {
        "name": "diego.com",
        "city": "Cercado/Cochabamba",
        "phone": "12345678",
        "time_zone": "Pacific/Midway",
        "province": "Province of the location",
        "state": "State of the location",
        "address": "test",
        "zipCode": "12345678",
        "fax": "12345678",
        "notes": "test_success",
        "countryCode": "AU",
        "eeo_applicable": 0
    }

    assert assert_location_schema_post(payload) == True
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 401

def test_location_patch_some_fields(test_login, set_up_patch_location):
    url = f'{system_url}{Endpoints.location.value}/{set_up_patch_location}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "name": "pruebas_patch.com",
        "city": "Diplomado/San Simon",
        "notes": "test_success",
        "countryCode": "AU",
    }
    response = OrangeRequests().patch(url=url, headers=headers, data=payload)
    assert response.status_code == 200
    assert assert_location_schema_patch_success(response.json()) == True


