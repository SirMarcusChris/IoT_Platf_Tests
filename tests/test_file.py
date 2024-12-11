# import requests
# import json
# import urllib3
#
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# url = "https://10.24.64.30/api/v1"
#
#
# #авторизация под админом
# payload = {'grant_type': 'password',
# 'username': 'admin',
# 'password': 'Test18plat34Form'}
# files=[
#
# ]
# headers = {
#   'Authorization': 'Basic YXBpLWNsaWVudDpwYXNzd29yZA=='
# }
#
# response = requests.request("POST", url=f'{url}/oauth2/token', headers=headers, data=payload,
# files=files, verify=False)
#
# admin_token = response.json()['access_token']
# print(f"Токен админа сохранён: {admin_token}")
#

