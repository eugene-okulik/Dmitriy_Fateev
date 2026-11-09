import requests
import allure
from test_api_fateev.endpoints.endpoint import EndPoint


class DeleteObject(EndPoint):

    @allure.step("Delete object")
    def delete_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(url=f"{self.url}/{object_id}", headers=headers)
        return self.response
