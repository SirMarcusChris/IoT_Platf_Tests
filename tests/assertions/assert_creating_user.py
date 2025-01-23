import pytest
import json
import requests

from tests.conftest import create_user_fixture


def assert_creating_user(response):
    response_json = response.json()
    assert response.status_code == 200
    assert isinstance(response.json()['id'], str)


def assert_get_users_list(response, user_id):
    response_json = response.json()
    assert response.status_code == 200
    assert 'data' in response_json
    assert isinstance(response_json['data'], list)
    # Проверяем, что в каждом элементе списка 'data' есть 'id'
    for users in response_json['data']:
        assert 'id' in users
    assert response_json['total'] > 1
    assert any(user["roleName"] == "Абонент" for user in response_json["data"])
    assert user_id == 

    # Создаём список user_id из данных
    # user_ids = [user['id'] for user in response_json['data']]
    # Проверяем, что user_id, который мы получили ранее, есть в списке пользователей
    # assert user_id in user_ids  # Убеждаемся, что наш user_id присутствует в списке