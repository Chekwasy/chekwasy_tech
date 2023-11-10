#!/usr/bin/python3
""" holds class solar"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from hashlib import md5


class Solar(BaseModel, Base):
    """Representation of a Solar user """
    if models.storage_t == 'db':
        __tablename__ = 'solar_users'
        email = Column(String(128), nullable=True)
        password = Column(String(128), nullable=True)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        phone = Column(String(128), nullable=True)
        amount = Column(Integer, nullable=True, default=0)
        state = Column(String(128), nullable=True)
        city = Column(String(128), nullable=True)
        street = Column(String(128), nullable=True)
        others = Column(String(200), nullable=True)

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        phone = ""
        amount = 0
        state = ""
        city = ""
        street = ""
        others = ""

    def __init__(self, *args, **kwargs):
        """initializes solar user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
