from pydantic import BaseModel
from typing import Optional

class AdminAuth(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
    expires_in: int

class AdminAuthEmptyBody(BaseModel):
    error_description: str
    error: str
    error_uri: str


