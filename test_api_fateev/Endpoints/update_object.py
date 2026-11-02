import allure
import requests

from Endpoints.endpoint import EndPoint


class UpdateObject(EndPoint):
    url = f"{EndPoint.url}/object"

    @allure.step("Update object with put method")
    def put_method(self, body, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(url=f"{self.url}/{post_id}", json=body, headers=headers)
        assert self.response.json()['name'] == body['name']
        return self.response

    @allure.step("Update object with patch method")
    def patch_method(self, body, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(url=f"{self.url}/{post_id}", json=body, headers=headers)
        return self.response
