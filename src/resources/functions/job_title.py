import random
import string

import pytest

from conftest import *


def ramdom_info(value):
    data = ''.join(random.choices(string.ascii_lowercase + string.digits, k=value))
    return data


def set_up_delete(login):
    url = f'{system_url}{Endpoints.job_titles.value}'
    headers = {'Authorization': f'{login}'}
    params = {'limit': 1, 'sortingField': 'id'}
    response = OrangeRequests().get(url, headers=headers, params=params)
    response_data = response.json()
    data = response_data["data"][0]
    return [str(data["id"]), {
            "jobTitleName": data["jobTitleName"],
            "jobDescription": data["jobDescription"],
            "note": data["note"]
        }]
