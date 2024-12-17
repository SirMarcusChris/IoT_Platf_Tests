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
        AdminAuth(**response.json())
    except ValidationError as e:
        raise ValidationError(f"Response validation failed: {e}")


def test_admin_authorization_with_empty_data(api_client):
    headers = {
        'Authorization': 'Basic YXBpLWNsaWVudDpwYXNzd29yZA=='
    }
    data = {}  # empty body
    response = api_client.admin_auth_for_test(headers=headers, data=data)
    assert response.status_code == 400