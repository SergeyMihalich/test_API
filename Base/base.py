import requests



class BaseClass:

    def get_request(self, URL):
        return requests.get(URL)

    def post_request(self, URL, payload):
        return requests.post(URL, json=payload)

    def put_request(self, URL, payload):
        return requests.put(URL, json=payload)

    def del_request(self, URL):
        return requests.delete(URL)

    def patch_request(self, URL, payload):
        return requests.patch(URL, json=payload)