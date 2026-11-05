import requests
import allure
from Endpoints.endpoint import EndPoint


class GetObject(EndPoint):
    @allure.step("Get all objects")
    def request_to_url(self):
        self.response = requests.get(self.url)
        return self.response
