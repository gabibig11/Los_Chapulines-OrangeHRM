from config import *
from conftest import *
from src.assertions.location_assertions import *
from src.orangeHRM_api.api_requests import OrangeRequests


@pytest.mark.smoke
def test_location_post_success(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
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
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 201
    assert assert_location_schema_post_reponse(response.json()) == True
    post_teardown(url=url, headers=headers, response=response.json(), attribute_search="id", attribute_delete="data",
                  array=True)


def test_post_location_without_name(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
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
    }
    assert assert_location_schema_post(payload) == False
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_post_location_without_countryCode(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
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
    }
    assert assert_location_schema_post(payload) == False
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_post_location_without_city(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
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
    }
    assert assert_location_schema_post(payload) == False
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_post_location_without_zipCode(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
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
    }
    assert assert_location_schema_post(payload) == False
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_post_location_without_timezone(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
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
    }
    assert assert_location_schema_post(payload) == False
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_post_location_invented_timezone(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
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
    }
    assert assert_location_schema_post(payload) == True
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_location_post_maximum_exceed(test_login):
        url = f'{system_url}{Endpoints.location.value}'
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
        response = OrangeRequests().post(url=url, headers=headers, data=payload)
        assert response.status_code == 400


def test_location_post_limit_maximum(test_login):
    url = f'{system_url}{Endpoints.location.value}'
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
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 201
    assert assert_location_schema_post_reponse(response.json()) == True
    post_teardown(url=url, headers=headers, response=response.json(), attribute_search="id", attribute_delete="data",
                  array=True)


def test_location_post_without_field_non_mandatory(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
    payload = {
        "name": "diego.com",
        "city": "Cercado/Cochabamba",
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

    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 201
    assert assert_location_schema_post_reponse(response.json()) == True
    post_teardown(url=url, headers=headers, response=response.json(), attribute_search="id", attribute_delete="data",
                  array=True)


def test_location_post_field_invented(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{test_login}'}
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
        "emergency_contact": "444 601 305 08",
        "eeo_applicable": 0
    }
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 400


def test_location_post_token_invented(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{random_token}'}
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
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 401


def test_location_post_token_expired(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Content-Type': 'application/json', 'Authorization': f'{expired_token}'}
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
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 401


def test_location_post_without_token(test_login):
    url = f'{system_url}{Endpoints.location.value}'
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
    response = OrangeRequests().post(url=url, headers=headers, data=payload)
    assert response.status_code == 401







