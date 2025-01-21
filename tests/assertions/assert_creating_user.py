import pytest
import json
import requests

def assert_creating_user(response):
    response_json = response.json()
    assert response.status_code == 200
    assert isinstance(response.json()['id'], str)
    assert 'id' in response.json()
    user_id = response.json()['id']
    return user_id
    
    
def assert_get_users_list(response):
    response_json = response.json()
    assert response.status_code == 200
    assert 'data' in response_json
    assert isinstance(response_json['data'], list)
    # Проверяем, что в каждом элементе списка 'data' есть 'id'
    for users in response_json['data']:
        assert 'id' in users
    assert response_json['total'] > 1
    assert any(user["roleName"] == "Абонент" for user in response_json["data"])
    # assert assert_creating_user(user_id)

    # Создаём список user_id из данных
    # user_ids = [user['id'] for user in response_json['data']]
    # Проверяем, что user_id, который мы получили ранее, есть в списке пользователей
    # assert user_id in user_ids  # Убеждаемся, что наш user_id присутствует в списке