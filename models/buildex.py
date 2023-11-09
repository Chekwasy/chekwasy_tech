#!/usr/bin/python3
""" holds class buildex"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class Buildex(BaseModel, Base):
    """Representation of a Buildex user """
    if models.storage_t == 'db':
        __tablename__ = 'buildex_users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        phone = Column(String(128), nullable=False)
        proposed_build = Column(String(128), nullable=False)
        land_area = Column(String(128), nullable=False)
        build_area = Column(String(128), nullable=False)
        room = Column(Integer, nullable=False, default=0)
        bathroom = Column(Integer, nullable=False, default=0)
        state = Column(String(128), nullable=False)
        city = Column(String(128), nullable=False)
        others = Column(String(200), nullable=False)

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        phone = ""
        proposed_build = ""
        land_area = ""
        build_area = ""
        room = 0
        bathroom = 0
        state = ""
        city = ""
        others = ""

    def __init__(self, *args, **kwargs):
        """initializes buildex user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
