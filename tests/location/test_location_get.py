import requests
import pytest
import jsonschema
from config import *
from src.assertions.location_assertions import *
from src.orangeHRM_api.api_requests import OrangeRequests
from src.orangeHRM_api.endpoints import Endpoints
from src.resources.functions.location import *


@pytest.mark.smoke
def test_get_all_locations(test_login):
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Authorization': f'{test_login}'}

    count_obj= int(num_object(url=url, headers=headers))
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(), count_obj)
    assert response.status_code == 200

def test_get_locations_invalid_token():
    url = f'{system_url}{Endpoints.location.value}'
    headers = {'Authorization': f'{random_token}'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 401

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
    assert response.status_code == 200


def test_get_location_filter_city(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=West%Briannetown'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_location_filter(response.json(), "city", "West Briannetown")
    assert response.status_code == 200


def test_get_location_filter_countryCode(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[country]=BR'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_location_filter(response.json(), "countryCode", "BR")
    assert response.status_code == 200


def test_get_location_filter_id(test_login):
    headers = {'Authorization': f'{test_login}'}

    url_object_random = f'{system_url}{Endpoints.location.value}'
    random_object = object_random(url=url_object_random, headers=headers)
    id_object = id_object_value(random_object=random_object)

    url = f'{system_url}{Endpoints.location.value}/{id_object}'
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_id_schema(response.json()) == True
    assert_location_id(response=response.json(), filter="id", value_filter=id_object)
    assert response.status_code == 200

def test_get_location_filter_name_value_non_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[name]=diego.sandy'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert response.status_code == 200


def test_get_location_filter_city_value_non_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=Punata'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert response.status_code == 200

def test_get_location_filter_countryCode_value_non_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[country]=XC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert response.status_code == 200


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
    assert response.status_code == 200

def test_get_location_filter_name_city_country_invalid_token(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=South%Shawna&filter[name]=alanis.info&filter[country]=AU'
    headers = {'Authorization': f'{random_token}'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 401


def test_get_location_filter_name_non_existent_city_country_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=Broderickberg&filter[name]=camila.adri.ville&filter[country]=AU'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert response.status_code == 200

def test_get_location_filter_name_city_non_existent_country_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=Tiquipaya&filter[name]=adri.villena&filter[country]=BR'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert response.status_code == 200

def test_get_location_filter_name_city_country_non_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=Sacaba&filter[name]=camila.villena&filter[country]=YZ'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert response.status_code == 200

def test_get_location_filter_city_existent_name_country_non_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=Concord&filter[name]=ivan.castroalc&filter[country]=RJ'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert response.status_code == 200

def test_get_location_filter_name_city_existent_country_non_existent(test_login):
    url = f'{system_url}{Endpoints.location.value}?filter[city]=North%Ollieview&filter[name]=price.info&filter[country]=RJ'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert_data_empty(response.json())
    assert response.status_code == 200


def test_location_filter_sortingby_ASC_sortingfield_name(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=name&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter(response.json(), "name", "ASC")
    assert response.status_code == 200

@pytest.mark.xfail(reason= "Error en la petición con filtro de orden “Ascendente” por “id” en location-H402-Verificar que Verificar que me devuelva los datos de las locaciones son ordenados ASC de acuerdo al atributo id")
def test_location_filter_sortingby_ASC_sortingfield_id(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=id&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter_id(response.json(),  "ASC")
    assert response.status_code == 200

def test_location_filter_sortingby_ASC_sortingfield_city(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=city&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter(response.json(), "city", "ASC")
    assert response.status_code == 200

@pytest.mark.xfail(reason= "Error en la petición con filtro de orden “Ascendente” por “countryCode” en location- H402 -Verificar que me devuelva los datos de las locaciones son ordenados ASC de acuerdo al atributo country")
def test_location_filter_sortingby_ASC_sortingfield_country_code(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingField=country&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert response.status_code == 200
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter(response.json(), "countryCode", "ASC")
    assert response.status_code == 200

@pytest.mark.xfail(reason= "Error en la petición con filtro de orden “Descendente” por “id” en location- 402 --Verificar que Verificar que me devuelva los datos de las locaciones son ordenados DESC de acuerdo al atributo id")
def test_location_filter_sortingby_DESC_sortingfield_id(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=id&sortingOrder=ASC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter_id(response.json(),  "DESC")
    assert response.status_code == 200
def test_location_filter_sortingby_DESC_sortingfield_name(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=name&sortingOrder=DESC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter(response.json(), "name", "DESC")
    assert response.status_code == 200

def test_location_filter_sortingby_DESC_sortingfield_city(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=city&sortingOrder=DESC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter(response.json(), "city", "DESC")
    assert response.status_code == 200

@pytest.mark.xfail(reason= "Error en la petición con filtro de orden “Descendente” por “countryCode” en location-402-Verificar que me devuelva los datos de las locaciones son ordenados DESC de acuerdo al atributo country")
def test_location_filter_sortingby_DESC_sortingfield_country_code(test_login):
    url = f'{system_url}{Endpoints.location.value}?sortingField=country&sortingOrder=DESC'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_orderby_orderfilter(response.json(), "countryCode", "DESC")
    assert response.status_code == 200

def test_location_filter_sortingby_ASC_sortingfield_name_limit(test_login):
    limit= int(limit_random(1,15))
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=name&sortingOrder=ASC&limit={limit}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(),count=limit)
    assert_orderby_orderfilter(response.json(), "name", "ASC")
    assert response.status_code == 200

def test_location_filter_sortingby_ASC_sortingfield_city_limit(test_login):
    limit = int(limit_random(1, 15))
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=city&sortingOrder=ASC&limit={limit}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(),count=limit)
    assert_orderby_orderfilter(response.json(), "city", "ASC")
    assert response.status_code == 200

@pytest.mark.xfail(reason="Error en la petición con filtro de orden “Descendente” por “countryCode” en location-402- Verificar que me devuelva los datos de un límite de locaciones ordenados ASC de acuerdo al atributo country")
def test_location_filter_sortingby_ASC_sortingfield_country_code_limit(test_login):
    limit = int(limit_random(1, 15))
    url = f'{system_url}{Endpoints.location.value}sortingField=country&sortingOrder=ASC&limit={limit}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(), count=limit)
    assert_orderby_orderfilter(response.json(), "countryCode", "ASC")
    assert response.status_code == 200

def test_location_filter_sortingby_DESC_sortingfield_name_limit(test_login):
    limit = int(limit_random(1, 15))
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=name&sortingOrder=DESC&limit={limit}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(), count=limit)
    assert_orderby_orderfilter(response.json(), "name", "DESC")
    assert response.status_code == 200

def test_location_filter_sortingby_DESC_sortingfield_city_limit(test_login):
    limit = int(limit_random(1, 15))
    url = f'{system_url}{Endpoints.location.value}?sortingFeild=city&sortingOrder=DESC&limit={limit}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(), count=limit)
    assert_orderby_orderfilter(response.json(), "city", "DESC")
    assert response.status_code == 200

@pytest.mark.xfail(reason= " Error en la petición con filtro de orden “Descendente” por “countryCode” en location y límite de objetos -402- Verificar que me devuelva los datos de un límite de locaciones son ordenados DESC de acuerdo al atributo country")
def test_location_filter_sortingby_DESC_sortingfield_country_code_limit(test_login):
    limit = int(limit_random(1, 15))
    url = f'{system_url}{Endpoints.location.value}sortingField=country&sortingOrder=DESC&limit={limit}'
    headers = {'Authorization': f'{test_login}'}
    response = OrangeRequests().get(url, headers=headers)
    assert assert_location_schema(response.json()) == True
    assert_count_obj(response.json(), count=limit)
    assert_orderby_orderfilter(response.json(), "countryCode", "DESC")
    assert response.status_code == 200

