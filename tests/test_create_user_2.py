import pytest
import json
import requests
from core.clients.api_client import ApiClient
from tests.actions.create_user_actions import create_user, get_users_list, delete_user
import tests.actions.create_user_actions
from faker import Faker
from tests.assertions.assert_creating_user import assert_get_users_list, assert_creating_user


def test_creating_user(get_admin_access_token):  # здесь пишутся только фикстуры
    faker = Faker()
    username = faker.first_name()
    user_id = create_user(client=get_admin_access_token, username=username)['id']# это вызов функции, здесь параметры для функции
    response = get_users_list(get_admin_access_token)
    assert_get_users_list(response=response,user_id=user_id)


def test_delete_user(get_admin_access_token):
    """Создаем пользователя и записываем его id"""
    faker = Faker()
    username = faker.first_name()
    user_data = create_user(client=get_admin_access_token, username=username)
    user_id = user_data["id"]
    response = get_users_list(get_admin_access_token)
    assert_get_users_list(response=response, user_id=user_id)
    """Удаляем пользователя"""
    delete_response = get_admin_access_token.delete_user_by_id(user_id=user_id)

    """Проверяем, что код ответа равен 204"""
    assert delete_response == 204, f"Ожидался код 204, но получили {delete_response}"
    """Получаем список пользователей и проверяем, что удаленный пользователь отсутствует"""
    users_list_response = get_admin_access_token.get_users()
    assert users_list_response.status_code == 200, f"Ошибка при получении списка пользователей: {users_list_response.text}"
    users_list = users_list_response.json().get("data", [])
    """Проверяем, что пользователь удален"""
    assert delete_user()


# def test_getting_users_list(get_admin_access_token):  # в этом тесте нужно будет снова создать пользователя,
#     # тк предыдущие тесты не должны быть завязаны на создании другого теста.
#     response = get_users_list(get_admin_access_token)
#     assert_get_users_list(response=response)
#

# def test_creating_user_with_same_username(api_client):  # creating an already exist user
#     client = ApiClient()
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {api_client.admin_auth()}'
#     }
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
#         "username": "ssss2s22"
#     })
#     response = client.create_user(headers=headers, data=data)
#     assert response.status_code == 500
#
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
