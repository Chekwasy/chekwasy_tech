#!/usr/bin/env python3
"""A module for authentication-related routines.
"""
import models
import bcrypt
from uuid import uuid4
from typing import Union, List, TypeVar
import datetime
import os
from sqlalchemy.orm.exc import NoResultFound
from models.farm import Farm
from models.buildex import Buildex
from models.solar import Solar
from models.annie import Annie
time = "%Y-%m-%dT%H:%M:%S.%f"



def _hash_password(password: str) -> bytes:
    """Hashes a password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """generate a uuid for return"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = models.storage

    def register_farm_user(self, email: str, password: str) -> Farm:
        """method to hash pwd, create farm user and return user"""
        hsh_pwd = _hash_password(password)
        try:
            self._db.find_farm_user_by(email=email)
        except NoResultFound:
            return self._db.add_farm_user(email, hsh_pwd)
        raise ValueError("User " + email + " already exists")

    def valid_farm_login(self, email: str, password: str) -> bool:
        """validate a farm login given email and pwd"""
        try:
            usr = self._db.find_farm_user_by(email=email)
            enc = str(password).encode("utf-8")
            if bcrypt.checkpw(enc, usr.hashed_password.encode()):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_farm_session(self, email: str) -> str:
        """create a farm session for an email"""
        try:
            usr = self._db.find_farm_user_by(email=email)
            uid = _generate_uuid()
            t = datetime.datetime.utcnow()
            self._db.update_farm_user(usr.id, farm_session_id=uid, session_created_at=t)
            return uid
        except NoResultFound:
            return None
        return None

    def get_farm_user_from_session_id(self, farm_session_id: str) -> Farm:
        """return a farm user based on a session_id"""
        if farm_session_id is None:
            return None
        try:
            usr = self._db.find_farm_user_by(farm_session_id=farm_session_id)
            if self._db.session_duration <= 0:
                return usr
            cur_time = datetime.datetime.utcnow()
            time_span = datetime.timedelta(seconds=self._db.session_duration)
            exp_time = usr.session_created_at + time_span
            if exp_time < cur_time:
                return None
            return usr
        except NoResultFound:
            return None

    def destroy_farm_session(self, user_id: str) -> None:
        """destroy the farm session by changing the
session in db to none"""
        if user_id is None:
            return None
        try:
            usr = self._db.find_farm_user_by(id=user_id)
            self._db.update_farm_user(usr.id, farm_session_id=None)
            return None
        except NoResultFound:
            return None

    def get_farm_reset_password_token(self, email: str) -> str:
        """get a farm reset password token for an email"""
        try:
            usr = self._db.find_farm_user_by(email=email)
            uid = _generate_uuid()
            self._db.update_farm_user(usr.id, reset_token=uid)
            return uid
        except NoResultFound:
            raise ValueError
        return None


    def update_farm_password(self, reset_token: str, password: str) -> None:
        """update farm password via reset token"""
        try:
            usr = self._db.find_farm_user_by(reset_token=reset_token)
            hsh_pw = _hash_password(password)
            self._db.update_farm_user(
                usr.id, hashed_password=hsh_pw, reset_token=None)
            return None
        except NoResultFound:
            raise ValueError

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth method - that returns False - path and excluded_paths
        will be used"""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        if (path + "/") in excluded_paths:
            return False
        if (path[:-1]) in excluded_paths:
            return False
        for b in excluded_paths:
            if "*" in b:
                rout = b.split("*")
                if path.startswith(rout[0]):
                    return False
                rout = []
        return True

    def current_farm_user(self, request=None) -> TypeVar('Farm'):
        """that returns None - request will be the Flask request object"""
        if request is None:
            return None
        sess_id = self.session_cookie_farm(request)
        usr = self.get_farm_user_from_session_id(sess_id)
        if usr is None:
            return None
        return usr

    def session_cookie_farm(self, request=None):
        """returns cookie value from request for farm"""
        if request is None:
            return None
        cookie_name = os.getenv('FARM_SESSION_NAME')
        return request.cookies.get(cookie_name)

    def update_farm_usr(self, cooki: str, usr_dt: dict) -> None:
        """update farm user"""
        try:
            first_name = usr_dt.get("first_name")
            last_name = usr_dt.get("last_name")
            phone = usr_dt.get("phone")
            street = usr_dt.get("street")
            city = usr_dt.get("city")
            state = usr_dt.get("state")
            usr = self.get_farm_user_from_session_id(cooki)
            self._db.update_farm_user(
                usr.id, first_name=first_name, last_name=last_name, phone=phone, state=state, street=street, city=city)
            return None
        except NoResultFound:
            raise ValueError
