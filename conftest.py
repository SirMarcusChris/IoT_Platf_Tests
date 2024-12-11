from core.clients.api_client import ApiClient
import pytest

@pytest.fixture(scope="session")
def api_client():
    client = ApiClient()
    client.admin_auth()
    return client