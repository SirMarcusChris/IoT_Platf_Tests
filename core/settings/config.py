from enum import Enum


class Users(Enum):
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "Test18plat34Form"
    ADMIN_GRANT_TYPE = 'password'

    USER_USERNAME = "user"
    USER_PASSWORD = "admin"
    USER_GRANT_TYPE = 'password'

class GetAdminToken:

    def test_create_user(api_client):

        globals['access_token'] = api_client.admin_auth()

