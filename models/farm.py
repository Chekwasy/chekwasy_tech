#!/usr/bin/python3
""" holds class farm"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from hashlib import md5


class Farm(BaseModel, Base):
    """Representation of a farm user """
    if models.storage_t == 'db':
        __tablename__ = 'farm_users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        phone = Column(String(128), nullable=False)
        reference = Column(String(128), nullable=False)
        state = Column(String(128), nullable=False)
        city = Column(String(128), nullable=False)
        street = Column(String(128), nullable=False)
        order_qty = Column(Integer, nullable=False, default=0)

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        phone = ""
        reference = ""
        state = ""
        city = ""
        street = ""
        order_qty = 0

    def __init__(self, *args, **kwargs):
        """initializes farm user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
