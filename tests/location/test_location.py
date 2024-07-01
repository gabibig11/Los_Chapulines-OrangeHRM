import requests
import pytest
import jsonschema
from config import system_url
from src.assertions.location_assertions import assert_location_schema, assert_location_id_schema, \
    assert_location_filter, assert_count_obj, assert_location_id, assert_ok, assert_data_empty, \
    assert_orderby_orderfilter, assert_orderby_orderfilter_id, assert_offset_orderby
from src.orangeHRM_api.api_requests import OrangeRequests
from src.orangeHRM_api.endpoints import Endpoints
@pytest.mark.smoke
def test_get_all_locations(test_login):
    count_obj=551
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(), count_obj)
    assert_ok(response)

def test_get_locations_invalid_token(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Authorization': f'{test_login}4'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 401
    assert response.json()['error'] == "invalid_token"
    assert response.json()['error_description'] == "The access token provided is invalid"

def test_get_location_token_empty():
    url = f'{system_url}{Endpoints.location.value}'
    headers = { }
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 401

def test_get_location_filter_name(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[name]=adonis.net'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_location_filter(response.json(), "name", "adonis.net")
    assert_ok(response)


def test_get_location_filter_city(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=West%Briannetown'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_location_filter(response.json(), "city", "West Briannetown")
    assert_ok(response)


def test_get_location_filter_countryCode(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[country]=BR'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_location_filter(response.json(), "countryCode", "BR")
    assert_ok(response)


def test_get_location_filter_id(test_login):
    url = f'{system_url}{Endpoints.location.value}/564'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_id_schema(response.json()) == True
    assert_location_id(response.json(), "id", "564")
    assert_ok(response)

def test_get_location_filter_name_value_non_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[name]=diego.sandy'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert_ok(response)


def test_get_location_filter_city_value_non_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=Punata'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert_ok(response)

def test_get_location_filter_countryCode_value_non_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[country]=XC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert_ok(response)


def test_get_location_filter_id_value_non_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}/1000'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 404


def test_get_location_filter_name_city_country(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=South%Shawna&filter[name]=alanis.info&filter[country]=AU'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_location_schema(response.json())
    assert_location_filter(response.json(), "city", "South Shawna")
    assert_location_filter(response.json(), "name", "alanis.info")
    assert_location_filter(response.json(), "countryCode", "AU")
    assert_ok(response)

def test_get_location_filter_name_city_country_invalid_token(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=South%Shawna&filter[name]=alanis.info&filter[country]=AU'
    headers = {'Authorization': f'{test_login}8'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 401
    assert response.json()['error'] == "invalid_token"
    assert response.json()['error_description'] == "The access token provided is invalid"


def test_get_location_filter_name_non_existent_city_country_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=Broderickberg&filter[name]=camila.adri.ville&filter[country]=AU'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert_ok(response)

def test_get_location_filter_name_city_non_existent_country_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=Tiquipaya&filter[name]=adri.villena&filter[country]=BR'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert_ok(response)

def test_get_location_filter_name_city_country_non_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=Sacaba&filter[name]=camila.villena&filter[country]=YZ'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert_ok(response)

def test_get_location_filter_city_existent_name_country_non_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=Concord&filter[name]=ivan.castroalc&filter[country]=RJ'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert_ok(response)

def test_get_location_filter_name_city_existent_country_non_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=North%Ollieview&filter[name]=price.info&filter[country]=RJ'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert_ok(response)


def test_location_filter_sortingby_ASC_sortingfield_name(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=name&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter(response.json(), "name", "ASC")
    assert_ok(response)

@pytest.mark.xfail
def test_location_filter_sortingby_ASC_sortingfield_id(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=id&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter_id(response.json(),  "ASC")
    assert_ok(response)

def test_location_filter_sortingby_ASC_sortingfield_city(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=city&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter(response.json(), "city", "ASC")
    assert_ok(response)

@pytest.mark.xfail
def test_location_filter_sortingby_ASC_sortingfield_country_code(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingField=country&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_ok(response)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter(response.json(), "countryCode", "ASC")
    assert_ok(response)

@pytest.mark.xfail
def test_location_filter_sortingby_DESC_sortingfield_id(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=id&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter_id(response.json(),  "DESC")
    assert_ok(response)
def test_location_filter_sortingby_DESC_sortingfield_name(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=name&sortingOrder=DESC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter(response.json(), "name", "DESC")
    assert_ok(response)

def test_location_filter_sortingby_DESC_sortingfield_city(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=city&sortingOrder=DESC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter(response.json(), "city", "DESC")
    assert_ok(response)

@pytest.mark.xfail
def test_location_filter_sortingby_DESC_sortingfield_country_code(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingField=country&sortingOrder=DESC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter(response.json(), "countryCode", "DESC")
    assert_ok(response)

def test_location_filter_sortingby_ASC_sortingfield_name_limit(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=name&sortingOrder=ASC&limit=6'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(),6)
    assert_orderby_orderfilter(response.json(), "name", "ASC")
    assert_ok(response)

def test_location_filter_sortingby_ASC_sortingfield_city_limit(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=city&sortingOrder=ASC&limit=5'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(), 5)
    assert_orderby_orderfilter(response.json(), "city", "ASC")
    assert_ok(response)

@pytest.mark.xfail
def test_location_filter_sortingby_ASC_sortingfield_country_code_limit(test_login):
    url = f'{system_url}{Endpoints.location.value}sortingField=country&sortingOrder=ASC&limit=10'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(), 10)
    assert_orderby_orderfilter(response.json(), "countryCode", "ASC")
    assert_ok(response)

def test_location_filter_sortingby_DESC_sortingfield_name_limit(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=name&sortingOrder=DESC&limit=3'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(),3)
    assert_orderby_orderfilter(response.json(), "name", "DESC")
    assert_ok(response)

def test_location_filter_sortingby_DESC_sortingfield_city_limit(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=city&sortingOrder=DESC&limit=8'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(), 8)
    assert_orderby_orderfilter(response.json(), "city", "DESC")
    assert_ok(response)

@pytest.mark.xfail
def test_location_filter_sortingby_DESC_sortingfield_country_code_limit(test_login):
    url = f'{system_url}{Endpoints.location.value}sortingField=country&sortingOrder=DESC&limit=9'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(), 9)
    assert_orderby_orderfilter(response.json(), "countryCode", "DESC")
    assert_ok(response)

