import requests
import allure
from test_api_fateev.endpoints.endpoint import EndPoint


class GetObject(EndPoint):
    @allure.step("Get all objects")
    def get_all_objects(self):
        self.response = requests.get(self.url)
        return self.response

    @allure.step("Get one object")
    def get_one_object(self, object_id):
        self.response = requests.get(f"{self.url}/{object_id}")
        return self.response
