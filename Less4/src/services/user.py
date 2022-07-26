import json
import uuid
from functools import lru_cache
from typing import Optional

from fastapi import Depends
from sqlmodel import Session

from src.api.v1.schemas import UserCreate, UserGeneral, UserModel
from src.db import AbstractCache, get_cache, get_session
from src.models import User
from src.services import ServiceMixin

__all__ = ("UserService", "get_user_service")


class UserService(ServiceMixin):

    def create_user(self, user: UserCreate) -> dict:
        """Создание пользователя."""
        new_user = User(username=user.username, password=user.password, email=user.email, uuid=str(uuid.uuid4()),
                        roles="")
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        new_user_dict = new_user.dict()
        del new_user_dict["id"]
        del new_user_dict["password"]
        new_user_dict["roles"] = []
        return new_user_dict

    def is_email(self, email: str) -> bool:
        """Проверить, зарегистрирован ли email."""
        user = self.session.query(User).filter(User.email == email).first()
        return bool(user)

    def is_username(self, username: str) -> bool:
        """Проверить, зарегистрирован ли username."""
        user = self.session.query(User).filter(User.username == username).first()
        return bool(user)

    def get_user(self, user) -> UserGeneral:
        """Получить user по логину и паролю."""
        user = self.session.query(User).filter(User.username == user.username, User.password == user.password).first()
        if user:
            user.roles = user.roles.split(",")
        return user

    def get_user_by_uuid(self, uuid) -> UserGeneral:
        """Получить user по uuid."""
        user = self.session.query(User).filter(User.uuid == uuid).first()
        if user:
            user.roles = user.roles.split(",")
        return user

    def change_fields(self, uuid, fields) -> UserGeneral:
        user = self.session.query(User).filter(User.uuid == uuid).first()
        for field_key, field_value in fields:
            setattr(user, field_key, field_value)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        if user:
            user.roles = user.roles.split(",")
        return user


# get_user_service — это провайдер UserService. Синглтон
@lru_cache()
def get_user_service(
    cache: AbstractCache = Depends(get_cache),
    session: Session = Depends(get_session),
) -> UserService:
    return UserService(cache=cache, session=session)
