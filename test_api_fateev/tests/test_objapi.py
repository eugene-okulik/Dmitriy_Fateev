import pytest
from data import PARAMETRIZE_DATA, DATA_PUT_METHOD, DATA_PATCH_METHOD


def test_get_one_object(get_object_endpoint, object_id):
    get_object_endpoint.get_one_object(object_id)
    get_object_endpoint.check_that_status_is_200()


def test_get_all_objects(get_object_endpoint):
    get_object_endpoint.get_all_objects()
    get_object_endpoint.check_that_status_is_200()


@pytest.mark.parametrize("color, size, name", PARAMETRIZE_DATA)
def test_add_object(create_object_endpoint, color, size, name):
    body = {"data": {"color": color, "size": size}, "name": name}
    create_object_endpoint.create_new_object(body)
    create_object_endpoint.check_that_status_is_200()
    assert create_object_endpoint.response.json()["name"] == name


def test_put_an_object(update_object_endpoint, object_id):
    update_object_endpoint.put_method(DATA_PUT_METHOD, object_id)
    update_object_endpoint.check_that_status_is_200()


def test_patch_an_object(update_object_endpoint, object_id):
    update_object_endpoint.patch_method(DATA_PATCH_METHOD, object_id)
    update_object_endpoint.check_that_status_is_200()


def test_delete_an_object(delete_object_endpoint, object_id):
    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_that_status_is_200()
