import random
import requests
import pytest

URL = 'http://objapi.course.qa-practice.com/object'
HEADERS = {'Content-Type': 'application/json'}


@pytest.fixture()
def new_object_id():
    body = {'data': {'color': 'black', 'size': 'small'}, 'name': 'new'}
    response = requests.post(URL, json=body, headers=HEADERS).json()
    object_id = response['id']
    print(object_id)
    yield object_id
    print('\ndeleting the object')
    requests.delete(f'{URL}/{object_id}')


@pytest.fixture(scope='session')
def start_finish_testing():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope='function')
def before_after_test():
    print('\nBefore test')
    yield
    print('\nAfter test')


@pytest.mark.smoke
def test_get_one_object(new_object_id, start_finish_testing, before_after_test):
    print('test')
    response = requests.get(f'{URL}/{new_object_id}').json()
    assert response['id'] == new_object_id


@pytest.mark.critical
def test_get_all_objects(before_after_test):
    print('test')
    response = requests.get(URL)
    assert response.status_code == 200


@pytest.mark.parametrize("color, size, name", [
    ("black", "big", "new"),
    ("white", "small", "second"),
    ("red", "medium", "third"), ])
def test_add_object(before_after_test, new_object_id, color, size, name):
    body = {"data": {"color": color, "size": size}, "name": name}
    response = requests.post(URL, json=body, headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["data"]["size"] == size


def test_put_an_object(before_after_test, new_object_id):
    body = {"data": {"color": "green", "size": "small"}, "name": "aboba"}
    response = requests.put(f'{URL}/{new_object_id}', json=body, headers=HEADERS).json()
    assert response['data']['color'] == 'green'


def test_patch_an_object(before_after_test, new_object_id):
    body = {"name": "Danil"}
    response = requests.patch(f'{URL}/{new_object_id}', json=body, headers=HEADERS).json()
    assert response['name'] == 'Danil'


def test_delete_an_object(before_after_test, new_object_id):
    response = requests.delete(f'{URL}/{new_object_id}')
    assert response.status_code == 200


@pytest.mark.regression
def test_one(before_after_test):
    assert 1 == 1


@pytest.mark.parametrize('logins', [random.randint(1, 5) for _ in range(5)])
def test_two(logins, before_after_test):
    print(logins)
    assert 1 == 1


@pytest.mark.medium
def test_three(before_after_test):
    assert 1 == 1
