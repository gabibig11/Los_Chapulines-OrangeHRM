import requests


class OrangeRequests:

    def get(self, url, headers):
        response = requests.get(url, headers)
        return response
