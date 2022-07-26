from datetime import datetime
from typing import Optional

from pydantic import BaseModel

__all__ = (
    "AccessToken",
    "RefreshToken",
    "UserCreate",
    "UserCreateResponse",
    "UserGeneral",
    "UserLogin",
    "UserModel",
    "UserTokenResponse",
    "UserView",
    "UserUpdate",
    "UserUpdateResponse"
)


class UserLogin(BaseModel):
    username: str
    password: str


class UserCreate(UserLogin):
    email: str


class UserModel(BaseModel):
    username: str
    roles: list[str] = []
    created_at: datetime
    is_superuser: bool
    uuid: str
    email: str


class UserModelFull(UserModel):
    is_totp_enabled: bool
    is_active: bool


class UserView(BaseModel):
    user: UserModel


class UserCreateResponse(BaseModel):
    msg: str
    user: UserModelFull


class UserTokenResponse(BaseModel):
    access_token: str
    refresh_token: str


class RefreshToken(BaseModel):
    refresh_token: str


class AccessToken(BaseModel):
    access_token: str


class UserTokenResponse(AccessToken, RefreshToken):
    ...


class UserUpdate(AccessToken):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None


class UserUpdateResponse(AccessToken):
    msg: str
    user: UserModelFull


class UserGeneral(UserModelFull):
    id: int
    password: str
