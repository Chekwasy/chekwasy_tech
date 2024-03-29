#!/usr/bin/python3
""" holds class farm"""

from datetime import datetime
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from hashlib import md5


class Farm(BaseModel, Base):
    """Representation of a farm user """
    if models.storage_t == 'db':
        __tablename__ = 'farm_users'
        email = Column(String(128), nullable=True)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        phone = Column(String(128), nullable=True)
        street = Column(String(300), nullable=True)
        state = Column(String(128), nullable=True)
        city = Column(String(128), nullable=True)
        order_qty = Column(Integer, nullable=True, default=0)
        hashed_password = Column(String(250), nullable=False)
        session_id = Column(String(250), nullable=True)
        session_created_at = Column(DateTime, default=datetime.utcnow)
        reset_token = Column(String(250), nullable=True)

    else:
        email = ""
        first_name = ""
        last_name = ""
        phone = ""
        street = ""
        state = ""
        city = ""
        order_qty = 0
        hashed_password = ""
        session_id = ""
        reset_token = ""


    def __init__(self, *args, **kwargs):
        """initializes farm user"""
        super().__init__(*args, **kwargs)
