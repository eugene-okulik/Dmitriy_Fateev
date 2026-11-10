import requests
import allure
from test_api_fateev.endpoints.endpoint import EndPoint


class CreateObject(EndPoint):

    @allure.step("Create object")
    def create_new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        return self.response

    @allure.step("Return object`s id")
    def get_object_id(self):
        return self.response.json()["id"]
