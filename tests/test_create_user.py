# import pytest
# import json
# import requests
# from core.clients import api_client
# from core.clients.api_client import ApiClient
#
# def test_creating_user(get_admin_access_token, api_client):
#
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {get_admin_access_token}'
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
#
#     response = client.create_user(headers=headers, data=data)
#     assert response.status_code == 200
#     assert isinstance(response.json()['id'], str)  # данный ассерт до конца не гарантирует, что id валидный. требуется созданным пользователем выполнить какое то действие, которое можно выпонить только с его токеном. и можно вынести создание пользователя как отдельное действие
#     assert 'id' in response.json()
#
#
#
# @pytest.mark.usefixtures("get_admin_access_token")
# def test_creating_user_with_same_username(get_admin_access_token):# creating an already exist user
#     client = ApiClient()
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {get_admin_access_token}'
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
# def test_creating_user_without_admin_token():
#     client = ApiClient()
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
#     response = client.create_user(headers=headers, data=data)
#     assert response.status_code == 401
#
#
#
# def test_getting_users_list(api_client):
#
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {api_client.admin_auth()}'
#     }
#     response = api_client.get_users(headers=headers)
#     assert response == 200
#
#
# def test_getting_users_by_id(get_admin_access_token):
#     client = ApiClient()
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {get_admin_access_token}'
#     }
#
#     response = client.get_users(headers=headers)
#     assert response == 200
