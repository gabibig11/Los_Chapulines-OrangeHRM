import requests

class OrangeRequests:

    def get(self, url, headers=None, params=None):
        response = requests.get(url, headers=headers, params=params)
        return response

    def post(self, url, headers=None, params=None, data=None):
        response = requests.post(url, headers=headers, params=params, data=data)
        return response
    
    def delete(self, url, headers=None, params=None, data=None):
        response = requests.delete(url, headers=headers, params=params, data=data)
        return response