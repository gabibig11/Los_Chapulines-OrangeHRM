import random
from src.orangeHRM_api.api_requests import OrangeRequests


def clean_data_location(item):
        return {
            "name": item.get("name"),
            "city": item.get("city"),
            "phone": item.get("phone"),
            "time_zone": item.get("time_zone"),
            "province": item.get("province"),
            "state": item.get("province"),
            "address": item.get("address"),
            "zipCode": item.get("zipCode"),
            "fax": item.get("fax"),
            "notes": item.get("notes"),
            "countryCode": item.get("countryCode"),
            "eeo_applicable": int(item.get("eeo_applicable"))
        }
def object_random(url, headers):
    response = OrangeRequests().get(url=url, headers=headers)
    assert response.status_code == 200
    data = response.json().get('data', [])
    random_index = random.randint(0, 551)
    random_object = data[random_index]
    return random_object

def id_object_value(random_object):
    id_object = random_object['id']
    return id_object


def limit_random(min_value, max_value):
    num_random= random.randint(min_value, max_value)
    return num_random

def num_object(url, headers):
    response= OrangeRequests().get(url=url, headers=headers)
    data= response.json()
    value_meta= data.get('meta', {})
    value_total= value_meta.get('total', None)
    return value_total

