import requests


class OrangeRequests:

    def get(self, url, headers=None):
        response = requests.get(url, headers=headers)
        return response
