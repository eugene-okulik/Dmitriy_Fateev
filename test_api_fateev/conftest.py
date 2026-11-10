import pytest

from endpoints.update_object import UpdateObject
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.delete_object import DeleteObject
from data import DEFAULT_DATA


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def object_id(create_object_endpoint):
    create_object_endpoint.create_new_object(DEFAULT_DATA)
    obj_id = create_object_endpoint.get_object_id()
    yield obj_id
    DeleteObject().delete_object(obj_id)
