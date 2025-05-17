import requests


class BaseMethods:

    # POST запрос
    @staticmethod
    def post_request(url, payload):
        return requests.post(url, json=payload)

    # POST запрос с заголовками
    @staticmethod
    def post_request_with_headers(url, payload, headers):
        return requests.post(url, json=payload, headers=headers)

    # GET запрос
    @staticmethod
    def get_request(url):
        return requests.get(url)

    # GET запрос с заголовками
    @staticmethod
    def get_request_with_headers(url, headers):
        return requests.get(url, headers=headers)

    # DELETE запрос
    @staticmethod
    def delete_request(url, headers):
        return requests.delete(url, headers=headers)

    # PATCH запрос
    @staticmethod
    def patch_request(url, headers, new_data):
        return requests.patch(url, headers=headers, json=new_data)

