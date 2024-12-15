from enum import Enum


class Users(Enum):
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "Test18plat34Form"
    ADMIN_GRANT_TYPE = 'password'

    USER_USERNAME = "user"
    USER_PASSWORD = "admin"
