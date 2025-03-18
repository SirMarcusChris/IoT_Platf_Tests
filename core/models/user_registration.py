from pydantic import BaseModel, Field
from typing import Dict, Any, List
from pydantic import EmailStr
from pydantic import validate_email

class RoleSettings(BaseModel):
    default_page: str = Field(..., alias="defaultPage")

class CreateUserSchema(BaseModel):
    access: Dict[str, Any]
    access_map: Dict[str, Any] = Field(..., alias="accessMap")
    additional_accounts: Dict[str, Any] = Field(..., alias="additionalAccounts")
    additional_email: List[EmailStr] = Field(..., alias="additionalEmail")
    admin: bool
    dashboard_items: List[Any] = Field(..., alias="dashboardItems")
    email: EmailStr
    email_confirm: bool = Field(..., alias="emailConfirm")
    enabled: bool
    house_ids: List[str] = Field(..., alias="houseIds")
    house_ids_with_refuser: List[str] = Field(..., alias="houseIdsWithRefuser")
    id: str
    language: str
    name: str
    password: str
    patronymic: str
    permissions: List[str]
    phone: str
    phone_confirm: bool = Field(..., alias="phoneConfirm")
    platforms: List[str]
    role: str
    role_id: str = Field(..., alias="roleId")
    role_name: str = Field(..., alias="roleName")
    role_settings: RoleSettings = Field(..., alias="roleSettings")
    status: str
    surname: str
    username: str