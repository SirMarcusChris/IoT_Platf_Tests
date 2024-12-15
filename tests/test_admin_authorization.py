from enum import verify

import pytest
import requests
from pydantic import ValidationError
from core.models.admin_auth_payload import AdminAuth

def test_admin_authorization(api_client):
    headers = {
        'Authorization': 'Basic YXBpLWNsaWVudDpwYXNzd29yZA=='
    }
    data = {
        "username": "admin",
        "password": "Test18plat34Form",
        "grant_type": "password"
    }

    response = api_client.admin_auth_for_test(headers=headers, data=data)
    try:
        AdminAuth(**response)
    except ValidationError as e:
        raise ValueError(response)