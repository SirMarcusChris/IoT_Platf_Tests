from enum import Enum


class Endpoints(Enum):
    AUTH_ENDPOINT = "/oauth2/token"
    HOUSE_ENDPOINT = "/houses"
    USERS = "/users"
