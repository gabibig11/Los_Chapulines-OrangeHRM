import pytest
from config import system_url
from src.assertions.getusers_assertions import (assert_getusers_id_schema, assert_getusers_id_include_schema,
                                                assert_getusers_filter_schema, assert_count_users,
                                                assert_getusers_filter_coincidences, assert_getusers_filter_order_all_values,
                                                assert_getusers_filter_include_schema)
from src.orangeHRM_api.endpoints import Endpoints
from src.orangeHRM_api.api_requests import OrangeRequests

@pytest.mark.smoke
def test_get_all_users(test_login):#test1 todos los usuarios al no poner parametro ni filtro
    token = test_login
    users_counted=162
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_count_users(response_data, users_counted)

@pytest.mark.xfail(reason="Erro de status code success en lugar de badrequest-H704-Verificar que la API devuelve un error 400 al proporcionar un filtro o parámetro no soportado")
def test_get_users_filter_not_params_supported(test_login):#test2 error al poner un parametro o filtro no soportado FAILED
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'invalidParam': 'invalid'
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    assert response.status_code == 400 #da un success en vez de un badrequest con el parametro no soportado

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
    users_counted=0
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[userOrEmpNamePartial]': '3312',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, users_counted)

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
    users_counted = 0
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[uname]': '3312',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, users_counted)

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
    users_counted = 0
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[employeeId]': '1000',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, users_counted)

def test_get_users_filter_ess_role_id(test_login):#test9 usuarios por filtro de Id de rol de usuario ESS REVISAR
    token = test_login
    user_role_id = '2'
    users_counted = 161
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[essrole]': user_role_id,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, users_counted)
    assert_getusers_filter_schema(response_data)
    #assert_getusers_filter_coincidences(response_data, user_role_id, 'user_role_id') #un usuario no cumple, tiene "user_role_id=1"

def test_get_users_filter_invalid_ess_role_id(test_login):#test10 ningun usuario por filtro de Id de rol de usuario ESS invalido o inexistente
    token = test_login
    users_counted = 0
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[essrole]': 5,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, users_counted)

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
    users_counted = 161
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[supervisorrole]': 3,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_count_users(response_data, users_counted)

def test_get_users_filter_invalid_supervisor_role_id(test_login):#test13 ningun usuario usuario por filtro de id de rol de supervisor invalido o inexistente
    token = test_login
    users_counted = 0
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[supervisorrole]': 5,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, users_counted)

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
    users_counted = 2
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[adminrole]': 1,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_count_users(response_data, users_counted)

def test_get_users_filter_invalid_admin_role_id(test_login):#test16 ningun usuario por filtro de id de rol de administrador invalido o inexistente
    token = test_login
    users_counted = 0
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[adminrole]': 5,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, users_counted)

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
    users_counted = 162
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
    assert_count_users(response_data, users_counted)

def test_get_users_filter_invalid_status(test_login):#test19 ningun usuario por filtro de estatus invalido o inexistente
    token = test_login
    users_counted = 0
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[status]': 0,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, users_counted)

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

def test_get_users_filter_location(test_login):#test21 usuarios por filtro de ubicacion
    token = test_login
    location = 4
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[location]': location,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)

@pytest.mark.xfail(reason="Error al validar ubicacion invalida que devuelve un usuario-H704-Verificar que la API no devuelve datos de usuarios al proporcionar un ID de ubicación inexistente en el filtro 'filter[location]'")
def test_get_users_filter_invalid_location(test_login):#test22 ningun usuario por filtro de ubicacion invalida o inexistente FAILED
    token = test_login
    users_counted = 0
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[location]': 1000000,
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, users_counted)# apesar de la ubicacion inexistente, devuele el usuario admin
def test_get_users_filter_include_deleted_false(test_login):#test23 usuario por filtro de eliminados en false
    token = test_login
    users_counted = 162
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[includeDeleted]': 'false',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_count_users(response_data, users_counted)

@pytest.mark.xfail(reason="Error en el parametro que no incluye usuarios eliminados-H704-Verificar que la API devuelve datos de los usuarios existentes incluyendo usuarios eliminados al proporcionar el valor “true” en el filtro 'filter[includeDeleted]'")
def test_get_users_filter_include_deleted_true(test_login):#test24 usuario por filtro de eliminados en true FAILED
    token = test_login
    users_counted = 0
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'filter[includeDeleted]': 'true',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_count_users(response_data, users_counted)# devuelve los 162 users como si fuera false

def test_get_users_filter_order_field_id(test_login):#test25 usuarios ordenados por id
    token = test_login
    users_counted = 162
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'orderField': 'id',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_count_users(response_data, users_counted)
    assert_getusers_filter_order_all_values(response_data, 'id')

def test_get_users_filter_order_field_user_name(test_login):#test26 usuarios ordenados por nombre de usuario
    token = test_login
    users_counted = 162
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'orderField': 'user_name',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_count_users(response_data, users_counted)
    assert_getusers_filter_order_all_values(response_data, 'user_name')

@pytest.mark.xfail(reason="Error 500 internal server error-H704-Verificar que la API devuelve datos de todos los usuarios ordenados por nombre a mostrar al proporcionar el parámetro 'orderField=display_name'")
def test_get_users_filter_order_field_display_name(test_login):#test27 usuarios ordenados por nombre de mostrado FAILED
    token = test_login
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'orderField': 'display_name',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200 #Bug Status code = 500

def test_get_users_filter_order_field_employee_last_name(test_login):#test28 usuarios ordenados por apellido de empleado
    token = test_login
    users_counted = 162
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'orderField': 'emp_lastName',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_count_users(response_data, users_counted)

def test_get_users_filter_order_field_status(test_login):#test29 usuarios ordenados por estatus
    token = test_login
    users_counted = 162
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'orderField': 'status',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_schema(response_data)
    assert_count_users(response_data, users_counted)
    assert_getusers_filter_order_all_values(response_data, 'status')

def test_get_users_filter_include(test_login):#test29 usuarios con mas detalles de su informacion
    token = test_login
    users_counted = 162
    url = f'{system_url}{Endpoints.getusers_filter.value}'
    params = {
        'include': 'Employee,UserUserRole,UserRole,Regions',
    }
    headers = {'Authorization': token}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert_getusers_filter_include_schema(response_data)
    assert_count_users(response_data, users_counted)