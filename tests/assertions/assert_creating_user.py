import pytest
import json
import requests


def assert_creating_user(response):
    response_json = response.json()
    assert response.status_code == 200
    assert isinstance(response.json()['id'], str)


def assert_get_users_list(response, user_id):
    assert response.status_code == 200
    response_json = response.json()  # Преобразуем в JSON
    assert 'data' in response_json  # Работаем с JSON
    assert isinstance(response_json['data'], list)
    for user in response_json['data']:
        assert 'id' in user
    assert response_json['total'] > 1


# def assert_user_created(response):
#     """Проверяет, что пользователь успешно создан"""
#     response_json = response.json()
#     assert response.status_code == 200, f"Ошибка создания пользователя: {response.text}"
#     assert "id" in response_json, "В ответе отсутствует ID пользователя"
#
#
# def assert_user_creation_failed(response):
#     """Проверяет, что создание пользователя без токена не выполняется"""
#     assert response.status_code == 401, f"Ожидался код 401, но получили {response.status_code}. Response: {response.text}"