import pytest
import requests

import core.clients.api_client
from core.clients import api_client




def test_create_house(api_client):
    headers = {
        'Authorization': f'Bearer {api_client.admin_auth()}',
    }

    data = {
        "id": "3",
        "roleId": "admin",
        "roleName": "Администратор",
        "username": "admin",
        "access": {},
        "accessMap": {},
        "houseIds": [],
        "houseIdsWithRefuser": [],
        "emailConfirm": False,
        "phoneConfirm": false,
        "password": null,
        "name": null,
        "surname": null,
        "patronymic": null,
        "email": null,
        "phone": null,
        "role": "admin",
        "status": "DEFAULT",
        "admin": true,
        "additionalAccounts": {},
        "language": "ru",
        "videoParameters": null,
        "permissions": [
            "view.users",
            "view.adminEvents",
            "view.controllers",
            "view.scriptPatterns",
            "view.serverSettings",
            "view.licenses",
            "view.organizations",
            "view.settings",
            "view.firmwares",
            "view.roles",
            "view.userStatistics",
            "view.videoPlatforms",
            "view.videoServerSettings",
            "needAllMeasures",
            "needHouseEvents",
            "needHousePage",
            "needHouseUsers",
            "needReportByAddresses",
            "needPersonalInformation",
            "admin",
            "canDeleteZWayDevicesForcibly",
            "canEditHouseGroupsAccesses",
            "user_statistics_w"
        ],
        "roleSettings": {
            "defaultPage": "view.users"
        },
        "enabled": true,
        "ownedHouseIds": [],
        "usingWebRtc": false,
        "testModeEnabled": false
    }
