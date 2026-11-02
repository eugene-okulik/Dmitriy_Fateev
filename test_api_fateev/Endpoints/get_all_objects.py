import requests
import allure
from Endpoints.endpoint import EndPoint


class GetObject(EndPoint):
    @allure.step("Get all objects")
    def request_to_objects(self):
        self.response = requests.get(self.url, headers=self.headers)
        return self.response
