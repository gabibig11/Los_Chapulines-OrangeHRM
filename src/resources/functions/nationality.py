import random
import string
import pytest

from src.orangeHRM_api.api_requests import OrangeRequests
from config import system_url
from src.orangeHRM_api.endpoints import Endpoints


def random_info(value):
    data = ''.join(random.choices(string.ascii_lowercase + string.digits, k=value))
    return data


def set_up_delete(login):
    url = f'{system_url}{Endpoints.nationality_list.value}'
    headers = {'Authorization': f'{login}'}
    params = {'limit': 3, 'sortingField': 'id'}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    data = response_data["data"]

    ids = [str(data[i]["id"]) for i in range(len(data))]  # Obtener todos los IDs
    # Ejemplo de datos a retornar, ajusta según lo que necesites
    example_data = {
        "name": data[0]["name"]
    }

    return ids, example_data


