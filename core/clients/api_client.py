import requests
import os
from dotenv import load_dotenv

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
            raise  ValueError(f"Unsupported environment: {environment}")

    def admin_auth(self):
        url = f"{self.base_url}{Endpoints.AUTH_ENDPOINT.value}"
        payload ={"username": Users.ADMIN_USERNAME.value, "password": Users.ADMIN_PASSWORD.value}
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        token = response.json().get("access_token")