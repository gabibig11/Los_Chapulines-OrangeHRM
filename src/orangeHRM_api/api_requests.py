import requests

class OrangeRequests:

    def get(self, url, headers=None):
        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def post(url, headers, payload):
        response = requests.post(url, headers=headers, data=payload)
        return response