import requests
import allure
from Endpoints.endpoint import EndPoint


class DeleteObject(EndPoint):
    url = f"{EndPoint.url}/object"

    @allure.step("Delete object")
    def delete_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(url=f"{self.url}/{object_id}", headers=headers)
        return self.response
