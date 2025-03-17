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


def assert_user_created(response):
    """Проверяет, что пользователь успешно создан"""
    response_json = response.json()
    assert response.status_code == 200, f"Ошибка создания пользователя: {response.text}"
    assert "id" in response_json, "В ответе отсутствует ID пользователя"


def assert_user_deleted(response, user_id, users_list):
    """Проверяет, что пользователь успешно удален (код 204)"""
    assert response.status_code == 204, f"Ожидался код 204, но получили {response.status_code}: {response.text}"
    # Проверяем, что user_id больше нет в списке пользователей
    user_exists = any(u["id"] == user_id for u in users_list)
    assert not user_exists, f"Пользователь с id {user_id} не был удален!"


def assert_user_creation_failed(response):
    """Проверяет, что создание пользователя без токена не выполняется"""
    assert response.status_code == 401, f"Ожидался код 401, но получили {response.status_code}. Response: {response.text}"