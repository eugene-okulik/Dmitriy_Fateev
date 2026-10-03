import requests

URL = 'http://objapi.course.qa-practice.com/object'
HEADERS = {'Content-Type': 'application/json'}


def new_post():
    body = {
        'data': {'color': 'black', 'size': 'small'}, 'name': 'new'
    }
    response = requests.post(URL, json=body, headers=HEADERS).json()
    return response['id']


def put_a_post():
    post_id = (new_post())
    body = {
        'data': {'color': 'black', 'size': 'big'}, 'id': post_id, 'name': 'alter'
    }
    response = requests.put(f'{URL}/{post_id}', json=body, headers=HEADERS).json()
    assert response['name'] == 'alter'


def patch_a_post():
    post_id = (new_post())
    body = {
        'name': 'aboba'
    }
    response = requests.patch(f'{URL}/{post_id}', json=body, headers=HEADERS).json()
    assert response['name'] == 'aboba'


def delete_a_post():
    post_id = (new_post())
    response = requests.delete(f"{URL}/{post_id}")
    assert response.status_code == 200


put_a_post()
patch_a_post()
delete_a_post()
