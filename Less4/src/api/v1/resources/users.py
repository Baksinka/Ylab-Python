import uuid
from datetime import datetime
from http import HTTPStatus
from typing import Optional

import jwt
from fastapi import APIRouter, Depends, HTTPException

from src.api.v1.schemas import (AccessToken, RefreshToken, UserCreate, UserCreateResponse, UserLogin,
                                UserTokenResponse, UserUpdate, UserUpdateResponse, UserView)
from src.core import config
from src.services import UserService, get_user_service

router = APIRouter()


@router.post(
    path="/signup",
    response_model=UserCreateResponse,
    summary="Регистрация пользователя",
    tags=["users"],
)
def user_signup(
    user: UserCreate, user_service: UserService = Depends(get_user_service),
) -> UserCreateResponse:
    if user_service.is_email(user.email):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="email is already registered")
    if user_service.is_username(user.username):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="username is already registered")
    user: dict = user_service.create_user(user=user)
    return UserCreateResponse(msg="User created.", user=user)


@router.post(
    path="/login",
    response_model=UserTokenResponse,
    summary="Авторизация пользователя",
    tags=["users"],
)
def user_login(
    user: UserLogin, user_service: UserService = Depends(get_user_service),
) -> UserTokenResponse:
    user = user_service.get_user(user)
    if not user:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="login or password does not correct")
    access_token, refresh_token = get_tokens(user.dict())
    return UserTokenResponse(access_token=access_token, refresh_token=refresh_token)


@router.post(
    path="/refresh",
    response_model=UserTokenResponse,
    summary="Обновление токенов",
    tags=["users"],
)
def user_login(
    token: RefreshToken, user_service: UserService = Depends(get_user_service),
) -> UserTokenResponse:
    data_refresh_token = decode_token(token.refresh_token)

    user = user_service.get_user_by_uuid(data_refresh_token["user_uuid"])
    if not user:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="token not correct")
    access_token, refresh_token = get_tokens(user.dict())
    return UserTokenResponse(access_token=access_token, refresh_token=refresh_token)


@router.get(
    path="/users/me",
    response_model=UserView,
    summary="Просмотр профиля пользователем",
    tags=["users"],
)
def user_view(
    access_token: str, user_service: UserService = Depends(get_user_service),
) -> UserView:
    data_access_token = decode_token(access_token)
    user = {
        "username": data_access_token["username"],
        "uuid": data_access_token["user_uuid"],
        "email": data_access_token["email"],
        "is_superuser": data_access_token["is_superuser"],
        "created_at": data_access_token["created_at"],
        "roles": data_access_token["roles"]
    }
    return UserView(user=user)


@router.put(
    path="/users/me",
    response_model=UserUpdateResponse,
    summary="Обновление профиля пользователем",
    tags=["users"],
)
def user_update(
    user: UserUpdate, user_service: UserService = Depends(get_user_service),
) -> UserUpdateResponse:
    data_access_token = decode_token(user.access_token)
    if getattr(user, "email", None):
        if user_service.is_email(user.email):
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="email is busy")
    else:
        delattr(user, "email")
    if getattr(user, "username", None):
        if user_service.is_username(user.username):
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="username is busy")
    else:
        delattr(user, "username")
    delattr(user, "access_token")
    user = user_service.change_fields(data_access_token["user_uuid"], user)
    access_token, refresh_token = get_tokens(user.dict(), refresh_uuid=data_access_token["refresh_uuid"])
    return UserUpdateResponse(msg="Update is successful. Please use new access_token.", user=user,
                              access_token=access_token)


def get_tokens(user, refresh_uuid=str(uuid.uuid4())):
    time_create_token = round(datetime.utcnow().timestamp())
    data_access_token = {
        "fresh": False,
        "username": user["username"],
        "user_uuid": user["uuid"],
        "email": user["email"],
        "is_superuser": user["is_superuser"],
        "created_at": str(user["created_at"]),
        "roles": user["roles"],
        "refresh": False,
        "type": "access",
        "iat": time_create_token,
        "nbf": time_create_token,
        "exp": time_create_token + config.JWT_ACCESS_TOKEN_TIME,
        "jti": str(uuid.uuid4()),
        "refresh_uuid": refresh_uuid
    }
    access_token = jwt.encode(data_access_token, config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM)
    data_refresh_token = {
        "fresh": False,
        "user_uuid": user["uuid"],
        "iat": time_create_token,
        "nbf": time_create_token,
        "jti": refresh_uuid,
        "exp": time_create_token + config.JWT_REFRESH_TOKEN_TIME,
        "type": "refresh"
    }
    refresh_token = jwt.encode(data_refresh_token, config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM)
    return access_token, refresh_token


def decode_token(token):
    try:
        data_token = jwt.decode(token.encode(), config.JWT_SECRET_KEY, algorithms=config.JWT_ALGORITHM)
    except Exception:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="problem with token")
    return data_token
