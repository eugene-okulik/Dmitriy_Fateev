import allure
import requests

from test_api_fateev.endpoints.endpoint import EndPoint


class UpdateObject(EndPoint):

    @allure.step("Update object with put method")
    def put_method(self, body, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(url=f"{self.url}/{object_id}", json=body, headers=headers)
        return self.response

    @allure.step("Update object with patch method")
    def patch_method(self, body, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(url=f"{self.url}/{object_id}", json=body, headers=headers)
        return self.response
