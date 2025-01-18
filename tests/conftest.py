from core.clients.api_client import ApiClient
import pytest
import requests

#from tests.create_user import admin_token


@pytest.fixture(scope="function")
def api_client():
    client = ApiClient()
    return client


@pytest.fixture(scope='function')  # Для получения разных типов токенов. В данном случае получается админский токен
def get_admin_access_token():
    client = ApiClient()
    token = client.admin_auth()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    client.session.headers = headers
    return client
