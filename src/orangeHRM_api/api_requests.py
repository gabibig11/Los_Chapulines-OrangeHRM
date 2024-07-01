import requests


class OrangeRequests:

    def get(self, url, headers=None, params=None):
        response = requests.get(url, headers=headers, params=params)
        return response

