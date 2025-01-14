import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://10.24.64.30/api/v1"


#авторизация под админом
payload = {'grant_type': 'password',
'username': 'admin',
'password': 'Test18plat34Form'}
files=[

]
headers = {
  'Authorization': 'Basic YXBpLWNsaWVudDpwYXNzd29yZA=='
}

response = requests.request("POST", url=f'{url}/oauth2/token', headers=headers, data=payload, files=files,
                            verify=False)

admin_token = response.json()['access_token']
print(f"Токен админа сохранён: {admin_token}")

#создание нового пользователя
payload = json.dumps({
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
  "name": "123wafweaqfqwf",
  "password": "123qwewqqwe",
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
  "username": "1122ssssssss432ss"
})


headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {admin_token}"
}



response = requests.request("POST", url=f'{url}/users', headers=headers, data=payload, verify=False)
print(response.status_code)

'''
#Авторизация под пользователем
payload = {'grant_type': 'password',
'username': 'plg',
'password': 'admin'}

headers = {
  'Authorization': 'Basic YXBpLWNsaWVudDpwYXNzd29yZA=='
}
'''



