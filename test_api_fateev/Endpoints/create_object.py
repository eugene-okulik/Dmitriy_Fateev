import requests
import allure
from Endpoints.endpoint import EndPoint


class CreateObject(EndPoint):
    url = f"{EndPoint.url}/object"

    @allure.step("Create object")
    def create_new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        return self.response

    @allure.step("Check that title is the same as sent")
    def check_response_name_is_correct(self, name):
        assert self.response.json()["name"] == name

    @allure.step("Return post_id")
    def get_object_id(self):
        return self.response.json()["id"]
