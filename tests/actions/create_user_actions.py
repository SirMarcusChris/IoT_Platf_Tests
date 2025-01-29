import json

from core.clients.api_client import ApiClient
from tests.assertions.assert_creating_user import assert_creating_user


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

    response = client.create_user_without_required_headers(data=data)
    assert_creating_user(response)
    return response.json()

def get_users_list(client: ApiClient):
    response = client.get_users()
    return response

# def creating_user_with_same_username(api_client):  # creating an already exist user
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