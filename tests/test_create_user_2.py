import pytest
import json
import requests
from core.clients.api_client import ApiClient
from tests.actions.user_actions import create_user, create_user_data
import tests.actions.user_actions
from faker import Faker
from tests.assertions.assert_creating_user import  assert_get_users_list, assert_creating_user, assert_user_deleted, assert_user_creation_failed


def test_creating_user(get_admin_access_token):  # здесь пишутся только фикстуры
    faker = Faker()
    username = faker.first_name()
    user_id = create_user(client=get_admin_access_token, username=username) # это вызов функции, здесь параметры для функции
    response = get_admin_access_token.get_users()  # Получаем список пользователей
    assert_get_users_list(response=response, user_id=user_id)  # Передаем response и user_id

def test_delete_user(get_admin_access_token):
    faker = Faker()
    username = faker.first_name()
    user_id = create_user(client=get_admin_access_token, username=username)  # это вызов функции, здесь параметры для функции
    response = get_admin_access_token.get_users()  # Получаем список пользователей
    assert_get_users_list(response=response, user_id=user_id)  #  Проверили что пользователь был создан




# def test_getting_users_list(get_admin_access_token):  # в этом тесте нужно будет снова создать пользователя,
#     # тк предыдущие тесты не должны быть завязаны на создании другого теста.
#     # Создаем нового пользователя
#     user_data = create_user_data(get_admin_access_token, "TestUser")
#     user_id = user_data["id"]  # Получаем его ID
#     response = get_users_list(get_admin_access_token)
#     assert_get_users_list(response=response,user_id=user_id)
#
# def test_creating_user_without_admin_token(api_client):
#     response = create_user_without_token(api_client)
#     assert_user_creation_failed(response)
#
#
# @pytest.mark.usefixtures("get_admin_access_token")
# def test_creating_user_with_same_username(get_admin_access_token, create_user_fixture):
#     user_id = create_user_fixture  # Фикстура возвращает user_id
#     # Получаем данные пользователя, чтобы узнать его username
#     response = get_admin_access_token.get_users()
#     assert response.status_code == 200, f"Ошибка при получении пользователей: {response.text}"
#     users = response.json().get("data", [])
#     user = next((u for u in users if u["id"] == user_id), None)
#     assert user, f"Не найден пользователь с id {user_id}"
#     username = user["username"]  # Теперь у нас есть username
#     # Пытаемся создать второго пользователя с тем же username
#     response = create_duplicate_user(get_admin_access_token, username)
#     assert response.status_code == 400, f"Ожидался код ошибки 400 при создании пользователя с уже существующим username, но получили {response.status_code}. Response: {response.text}"
#
# def test_creating_user_without_admin_token(api_client):
#     headers = {}
#     data = json.dumps({
#         "access": {},
#         "accessMap": {},
#         "additionalAccounts": {},
#         "additionalEmail": [
#             "string"
#         ],
#         "admin": False,
#         "dashboardItems": [],
#         "email": "",
#         "emailConfirm": False,
#         "enabled": True,
#         "houseIds": [],
#         "houseIdsWithRefuser": [],
#         "id": "",
#         "language": "ru",
#         "name": "",
#         "password": "123",
#         "patronymic": "",
#         "permissions": [
#             "view.dashboard",
#             "view.houses",
#             "view.scripts",
#             "view.devices",
#             "view.meters",
#             "view.events",
#             "view.settings",
#             "view.calculation",
#             "view.cameras",
#             "view.plans",
#             "needAllMeasures",
#             "needHeaderVariablesEditor",
#             "needReportByAddresses",
#             "minimizeDeviceInfoIfCharts",
#             "needPersonalInformation",
#             "computeDefaultPage",
#             "camera_w",
#             "controller_w",
#             "device_w",
#             "house_w",
#             "script_w"
#         ],
#         "phone": "",
#         "phoneConfirm": False,
#         "platforms": [],
#         "role": "user",
#         "roleId": "user",
#         "roleName": "Абонент",
#         "roleSettings": {
#             "defaultPage": "view.dashboard"
#         },
#         "status": "DEFAULT",
#         "surname": "",
#         "username": "11йys32ww120sep"
#     })
#     response = api_client.create_user(headers=headers, data=data)
#     assert response.status_code == 401
#
#
# def test_getting_users_by_id(api_client):
#     client = ApiClient()
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {api_client.admin_auth()}'
#     }
#
#     response = client.get_users(headers=headers)
#     assert response == 200
#
# @pytest.mark.usefixtures("get_admin_access_token")
# def test_delete_user(get_admin_access_token):
#     # Удаляем пользователя (проверки уже в assertions)
#     delete_user(get_admin_access_token)
