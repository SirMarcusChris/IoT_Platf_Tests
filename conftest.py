from core.clients.api_client import ApiClient
import pytest
import requests

from tests.create_user import admin_token


@pytest.fixture(scope='session')
def get_admin_access_token():
    client = ApiClient()
    token = client.admin_auth()
    return token
