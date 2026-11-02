import requests
import allure
from Endpoints.endpoint import EndPoint


class GetObject(EndPoint):
    @allure.step("Get all objects")
    def request_to_objects(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(self.url, headers=headers)
        return self.response
