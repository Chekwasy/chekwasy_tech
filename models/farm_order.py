#!/usr/bin/python3
""" holds class farm"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship


class Farm_order(BaseModel, Base):
    """Representation of a farm user order """
    if models.storage_t == 'db':
        __tablename__ = 'farm_users_orders'
        user_id = Column(String(60), ForeignKey('farm_users.id'), nullable=False)
        note = Column(String(500), nullable=False)
        order_qty = Column(Integer, nullable=True, default=0)

    else:
        user_id = ""
        order_qty = 0
        note = ""


    def __init__(self, *args, **kwargs):
        """initializes farm user"""
        super().__init__(*args, **kwargs)
