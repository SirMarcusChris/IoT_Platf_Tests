import pytest
import json
import requests

def assert_creating_user():
    assert response.status_code == 200
    assert isinstance(response.json()['id'], str)
    assert 'id' in response.json()

def assert_get_users_list():
    assert response.status_code == 200
    response_json = response.json()
    assert 'data' in response_json
    assert isinstance(response_json['data'], list)
    # Проверяем, что в каждом элементе списка 'data' есть 'id'
    for users in response_json['data']:
        assert 'id' in users