#!/usr/bin/python3
""" holds class annie"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class Annie(BaseModel, Base):
    """Representation of a Annie user """
    if models.storage_t == 'db':
        __tablename__ = 'annie_users'
        email = Column(String(128), nullable=True)
        password = Column(String(128), nullable=True)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        phone = Column(String(128), nullable=True)
        choice = Column(String(128), nullable=True)
        state = Column(String(128), nullable=True)
        city = Column(String(128), nullable=True)
        street = Column(String(128), nullable=True)
        link = Column(String(400), nullable=True)
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
        link = ""
        others = ""

    def __init__(self, *args, **kwargs):
        """initializes solar annie user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
