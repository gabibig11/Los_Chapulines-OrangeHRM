import pytest
from config import system_url
from src.assertions.getusers_assertions import (assert_getusers_id_schema, assert_getusers_id_include_schema,
                                                assert_getusers_filter_schema, assert_count_users,
                                                assert_getusers_filter_include_employee_schema,
                                                assert_getusers_filter_coincidences)
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests


def test_get_all_users(test_login):#test1 todos los usuarios al no poner parametro ni filtro
    token = test_login
    users_counted=157
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_count_users(response_data, users_counted)

def test_get_users_filter_not_params_supported(test_login):#test2 error al poner un parametro o filtro no soportado Failed
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'invalidParam': 'invalid'
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    assert response.status_code == 400

def test_get_users_filter_with_partial_name(test_login):#test3 usuarios filtrados por el nombre parcial
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[userOrEmpNamePartial]': 'Alb',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)

def test_get_users_filter_with_invalid_partial_name(test_login):#test4 ningun usuario al poner un filtro de nombre parcial invalido o no existente
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[userOrEmpNamePartial]': '3312',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, 0)

def test_get_users_filter_user_name(test_login):#test5 usuarios por filtro de nombre de usuario
    token = test_login
    user_name='Robertito'
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[uname]': user_name,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_getusers_filter_coincidences(response_data, user_name, "user_name")

def test_get_users_filter_invalid_user_name(test_login):#test6 ningun usuario por filtro con nombre de usuario invalido o inexistente
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[uname]': '3312',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, 0)

def test_get_users_filter_employee_id(test_login):#test7 usuarios por filtro de id de empleado
    token = test_login
    employee_id= '3'
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[employeeId]': employee_id,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_getusers_filter_coincidences(response_data, employee_id, 'emp_number')

def test_get_users_filter_invalid_employee_id(test_login):#test8 ningun usuario por filtro de id de empleado invalido o inexistente
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[employeeId]': '1000',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, 0)

def test_get_users_filter_ess_role_id(test_login):#test9 usuarios por filtro de Id de rol de usuario ESS REVISAR
    token = test_login
    user_role_id = 2
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[essrole]': user_role_id,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, 156)
    assert_getusers_filter_schema(response_data)
    """assert_getusers_filter_coincidences(response_data, user_role_id, 'user_role_id')"""

def test_get_users_filter_invalid_ess_role_id(test_login):#test10 ningun usuario por filtro de Id de rol de usuario ESS invalido o inexistente
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[essrole]': 5,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, 0)

def test_gte_users_filter_ess_role_id_not_supported(test_login):#test11 error al poner un filtro de id de rol ess no soportado
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[essrole]': 'idInvalido',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 422

def test_get_users_filter_supervisor_role_id(test_login):#test12 usuarios por filtro de id de rol de supervisor
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[supervisorrole]': 3,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_count_users(response_data, 156)

def test_get_users_filter_invalid_supervisor_role_id(test_login):#test13 ningun usuario usuario por filtro de id de rol de supervisor invalido o inexistente
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[supervisorrole]': 5,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, 0)

def test_get_users_filter_supervisor_role_id_not_supported(test_login):#test14 error al poner un filtro de id de rol de supervisor no soportado
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[supervisorrole]': 'idInvalido',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 422

def test_get_users_filter_admin_role_id(test_login):#test15 usuarios por filtro de id de rol de administrador
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[adminrole]': 1,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_count_users(response_data, 2)

def test_get_users_filter_invalid_admin_role_id(test_login):#test16 ningun usuario por filtro de id de rol de administrador invalido o inexistente
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[adminrole]': 5,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, 0)

def test_get_users_filter_admin_role_id_not_supported(test_login):#test17 error al poner un filtro de id de rol de administrador no soportado
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[adminrole]': 'idAdminInvalid',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 422

def test_get_users_filter_status(test_login):#test18 usuarios por filtro de estatus
    token = test_login
    status = 1
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[status]': status,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_count_users(response_data, 157)

def test_get_users_filter_invalid_status(test_login):#test19 ningun usuario por filtro de estatus invalido o inexistente
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[status]': 0,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, 0)

def test_get_users_filter_status_not_supported(test_login):#test20 error por filtro de estatus no soportado
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[status]': 'invalidStatus',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 422

