import json

from core.clients.api_client import ApiClient
from tests.assertions.assert_creating_user import assert_creating_user, assert_user_deleted


def create_user_data(client: ApiClient, username: str):  # Сообщаем, что переменная client принимает только значения класса ApiClient
    """Генерирует тело запроса для создания пользователя"""
    data = json.dumps({
        "access": {},
        "accessMap": {},
        "additionalAccounts": {},
        "additionalEmail": [
            "string"
        ],
        "admin": False,
        "dashboardItems": [],
        "email": "",
        "emailConfirm": False,
        "enabled": True,
        "houseIds": [],
        "houseIdsWithRefuser": [],
        "id": "",
        "language": "ru",
        "name": "",
        "password": "123",
        "patronymic": "",
        "permissions": [
            "view.dashboard",
            "view.houses",
            "view.scripts",
            "view.devices",
            "view.meters",
            "view.events",
            "view.settings",
            "view.calculation",
            "view.cameras",
            "view.plans",
            "needAllMeasures",
            "needHeaderVariablesEditor",
            "needReportByAddresses",
            "minimizeDeviceInfoIfCharts",
            "needPersonalInformation",
            "computeDefaultPage",
            "camera_w",
            "controller_w",
            "device_w",
            "house_w",
            "script_w"
        ],
        "phone": "",
        "phoneConfirm": False,
        "platforms": [],
        "role": "user",
        "roleId": "user",
        "roleName": "Абонент",
        "roleSettings": {
            "defaultPage": "view.dashboard"
        },
        "status": "DEFAULT",
        "surname": "",
        "username": username
    })

    response = client.create_user_without_required_headers(data=data)
    # assert_creating_user(response)
    return response.json()

def create_user_without_token(client: ApiClient, username: str):
    """Создает пользователя без токена"""
    data = json.dumps({
        "access": {},
        "accessMap": {},
        "additionalAccounts": {},
        "additionalEmail": ["string"],
        "admin": False,
        "dashboardItems": [],
        "email": "",
        "emailConfirm": False,
        "enabled": True,
        "houseIds": [],
        "houseIdsWithRefuser": [],
        "id": "",
        "language": "ru",
        "name": "",
        "password": "123",
        "patronymic": "",
        "permissions": [
            "view.dashboard",
            "view.houses",
            "view.scripts",
            "view.devices",
            "view.meters",
            "view.events",
            "view.settings",
            "view.calculation",
            "view.cameras",
            "view.plans",
            "needAllMeasures",
            "needHeaderVariablesEditor",
            "needReportByAddresses",
            "minimizeDeviceInfoIfCharts",
            "needPersonalInformation",
            "computeDefaultPage",
            "camera_w",
            "controller_w",
            "device_w",
            "house_w",
            "script_w"
        ],
        "phone": "",
        "phoneConfirm": False,
        "platforms": [],
        "role": "user",
        "roleId": "user",
        "roleName": "Абонент",
        "roleSettings": {"defaultPage": "view.dashboard"},
        "status": "DEFAULT",
        "surname": "",
        "username": "11йys32ww120sep"
    })
    headers = {}  # Отсутствуют заголовки аутентификации
    response = client.create_user(headers=headers, data=data)
    return response

def get_users_list(client: ApiClient):
    response = client.get_users()
    return response


def create_user(client: ApiClient, username: str):
    """Создает пользователя и возвращает его данные"""
    data = create_user_data(username)  #  Теперь передаем username в функцию
    response = client.create_user(headers=client.session.headers, data=data)
    return response


def create_duplicate_user(client: ApiClient, username: str):
    """Пытается создать пользователя с уже существующим username"""
    data = create_user_data(username)  # Повторно используем ту же функцию
    response = client.create_user(headers=client.session.headers, data=data)
    return response  # Возвращаем полный объект Response для теста




def delete_user(client: ApiClient):
    """Создает пользователя, получает его ID и удаляет"""
    user_data = create_user(client, "TestUser")
    user_id = user_data["id"]  # Получаем ID созданного пользователя
    headers = client.session.headers
    delete_url = f"{client.base_url}/users/{user_id}"
    response = client.session.delete(delete_url, headers=headers, verify=False)
    # Получаем список пользователей после удаления
    users_list_response = client.get_users()
    users_list = users_list_response.json().get("data", [])
    assert_user_deleted(response, user_id, users_list)  # Проверяем удаление
    return user_id  # Возвращаем ID удаленного пользователя для проверки