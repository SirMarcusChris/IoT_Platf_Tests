import pytest
import json
import requests
from core.clients import api_client


def test_creating_user(api_client):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': f'Bearer {api_client.admin_auth()}'
	}
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
		"username": "2111йys32w4rew3ewqr120sep"
	})
	
	response = api_client.create_user(headers=headers, data=data)
	assert response.status_code == 200
	assert isinstance(response.json()['id'], str)
	assert 'id' in response.json()


def test_creating_user_with_same_username(api_client):  # creating an already exist user
	headers = {
		'Content-Type': 'application/json',
		'Authorization': f'Bearer {api_client.admin_auth()}'
	}
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
		"username": "2111йys32w4rew3ewqr120sep"
	})
	response = api_client.create_user(headers=headers, data=data)
	assert response.status_code == 500


def test_creating_user_without_admin_token(api_client):
	headers = {}
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
		"username": "11йys32ww120sep"
	})
	response = api_client.create_user(headers=headers, data=data)
	assert response.status_code == 401


def test_getting_users_list(api_client):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': f'Bearer {api_client.admin_auth()}'
	}
	response = api_client.get_user(headers=headers)
	assert response == 200
    globals['id'] = response.json()['id']

def test_getting_users_by_id(api_client):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': f'Bearer {api_client.admin_auth()}'
	}
	response = api_client.get_user(headers=headers)
	assert response == 200
