from http.client import responses

import faker

from core.clients.api_client import ApiClient
import pytest
import requests
from faker import Faker

from tests.actions.user_actions import create_user


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


@pytest.fixture(scope='function')
def create_user_fixture(get_admin_access_token):
    # действия, которые создают пользователя
    faker=Faker()
    return create_user(client=get_admin_access_token,username=faker.first_name())['id']

