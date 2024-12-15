from pydantic import BaseModel
from typing import Optional

class AdminAuth(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
    expires_in: int

