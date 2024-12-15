from core.clients.api_client import ApiClient
import pytest
import requests

@pytest.fixture(scope="session")
def api_client():
    client = ApiClient()
    client.admin_auth()
    return client

