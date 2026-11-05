import pytest
from data import *


def test_get_one_object(create_object_endpoint):
    create_object_endpoint.create_new_object(DEFAULT_DATA)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_name_is_correct(DEFAULT_DATA["name"])


def test_get_all_objects(get_all_objects):
    get_all_objects.request_to_url()
    get_all_objects.check_that_status_is_200()


@pytest.mark.parametrize("color, size, name", PARAMETRIZE_DATA)
def test_add_object(create_object_endpoint, color, size, name):
    body = {"data": {"color": color, "size": size}, "name": name}
    create_object_endpoint.create_new_object(body)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_name_is_correct(body["name"])


def test_put_an_object(update_object_endpoint, object_id):
    update_object_endpoint.put_method(DATA_PUT_METHOD, object_id)
    update_object_endpoint.check_that_status_is_200()


def test_patch_an_object(update_object_endpoint, object_id):
    update_object_endpoint.patch_method(DATA_PATCH_METHOD, object_id)
    update_object_endpoint.check_that_status_is_200()


def test_delete_an_object(delete_object_endpoint, object_id):
    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_that_status_is_200()
