import pytest

from Endpoints.update_object import UpdateObject
from Endpoints.create_object import CreateObject
from Endpoints.get_all_objects import GetObject
from Endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def get_all_objects():
    return GetObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()
