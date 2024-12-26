import requests
import os
from dotenv import load_dotenv

import core.models.admin_auth_payload
from core.settings.config import Users
from core.settings.environments import Environment
from core.clients.endpoints import Endpoints

load_dotenv()


class ApiClient:
    def __init__(self):
        environment_str = os.getenv('ENVIRONMENT')
        try:
            environment = Environment[environment_str]
        except KeyError:
            raise ValueError(f"Unsupported environment value: {environment_str}")

        self.base_url = self.get_base_url(environment)
        self.session = requests.Session()

    def get_base_url(self, environment: Environment) -> str:
        if environment == Environment.TEST:
            return os.getenv('TEST_BASE_URL')
        elif environment == Environment.PROD:
            return os.getenv('PROD_BASE_URL')
        else:
            raise ValueError(f"Unsupported environment: {environment}")

    def admin_auth(self):
        url = f"{self.base_url}{Endpoints.AUTH_ENDPOINT.value}"
        data = {"username": Users.ADMIN_USERNAME.value, "password": Users.ADMIN_PASSWORD.value,
                "grant_type": Users.ADMIN_GRANT_TYPE.value}
        headers = {'Authorization': 'Basic YXBpLWNsaWVudDpwYXNzd29yZA=='}
        response = self.session.post(url, data=data, headers=headers, verify=False)
        response.raise_for_status()
        token = response.json()["access_token"]
        # assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
        return token

    def admin_auth_for_test(self, headers, data):
        url = f"{self.base_url}{Endpoints.AUTH_ENDPOINT.value}"
        response = self.session.post(url, headers=headers, data=data, verify=False)
        return response

    def user_auth(self):
        url = f"{self.base_url}{Endpoints.AUTH_ENDPOINT.value}"
        data = {"username": Users.USER_USERNAME.value, "password": Users.USER_PASSWORD.value,
                "grant_type": Users.USER_GRANT_TYPE.value}
        headers = {'Authorization': 'Basic YXBpLWNsaWVudDpwYXNzd29yZA=='}
        url = f"{self.base_url}{Endpoints.AUTH_ENDPOINT.value}"
        response = self.session.post(url, headers=headers, data=data, verify=False)
        return response

    def get_user(self, headers):
        url = f"{self.base_url}{Endpoints.USERS.value}"
        response = self.session.get(url, headers=headers, verify=False)
        return response.status_code

    def create_user(self, headers, data):
        url = f"{self.base_url}{Endpoints.USERS.value}"
        response = self.session.post(url, headers=headers, data=data, verify=False)
        return response
    
    def get_user_by_id(self, headers):
        url = f"{self.base_url}{Endpoints.USERS.value}"
        response = self.session.get(url, headers=headers, verify=False)
        return response.status_code