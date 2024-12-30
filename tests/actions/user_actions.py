import json

from core.clients.api_client import ApiClient


def create_user(client: ApiClient, username: str):  # Сообщаем, что переменная client принимает только значения класса ApiClient
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

    response = client.create_user_222222(data=data)
    assert response.status_code == 200
    assert isinstance(response.json()['id'], str)
    assert 'id' in response.json()