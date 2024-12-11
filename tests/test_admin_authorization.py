import pytest
import requests

def test_admin_autrorization(api_client):
    auth = api_client.admin_auth()
    assert auth == 200