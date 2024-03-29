#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from datetime import datetime
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import models
from models.farm import Farm
from models.base_model import BaseModel, Base
from models.buildex import Buildex
from models.solar import Solar
from models.annie import Annie
from models.farm_order import Farm_order
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine, tuple_
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Farm": Farm, "Buildex": Buildex,
           "Solar": Solar, "Annie": Annie, "Farm_order": Farm_order}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        CHEKWASY_MYSQL_USER = getenv('CHEKWASY_MYSQL_USER')
        CHEKWASY_MYSQL_PWD = getenv('CHEKWASY_MYSQL_PWD')
        CHEKWASY_MYSQL_HOST = getenv('CHEKWASY_MYSQL_HOST')
        CHEKWASY_MYSQL_DB = getenv('CHEKWASY_MYSQL_DB')
        CHEKWASY_ENV = getenv('CHEKWASY_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(CHEKWASY_MYSQL_USER,
                                             CHEKWASY_MYSQL_PWD,
                                             CHEKWASY_MYSQL_HOST,
                                             CHEKWASY_MYSQL_DB))
        if CHEKWASY_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        try:
            self.__session.add(obj)
        except Exception:
            self.__session.rollback()

    def save(self):
        """commit all changes of the current database session"""
        try:
            self.__session.commit()
        except Exception:
            self.__session.rollback()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

    def add_farm_user(self, email: str, hashed_password: str) -> Farm:
        """method to add farm user via email and hashd
password and saved to db"""
        try:
            dct = {}
            dct['email'] = email
            dct['hashed_password'] = hashed_password
            usr = Farm(**dct)

            usr.updated_at = datetime.utcnow()
            self.__session.add(usr)
            self.__session.commit()
            return usr
        except Exception:
            self.__session.rollback()
        return None

    def add_buildex_user(self, email: str, hashed_password: str) -> Buildex:
        """method to add buildex user via email and hashd
password and saved to db"""
        try:
            dct = {}
            dct['email'] = email
            dct['hashed_password'] = hashed_password
            usr = Buildex(**dct)

            usr.updated_at = datetime.utcnow()
            self.__session.add(usr)
            self.__session.commit()
            return usr
        except Exception:
            self.__session.rollback()
        return None

    def add_solar_user(self, email: str, hashed_password: str) -> Solar:
        """method to add farm user via email and hashd
password and saved to db"""
        try:
            dct = {}
            dct['email'] = email
            dct['hashed_password'] = hashed_password
            usr = Solar(**dct)

            usr.updated_at = datetime.utcnow()
            self.__session.add(usr)
            self.__session.commit()
            return usr
        except Exception:
            self.__session.rollback()
        return None

    def add_annie_user(self, email: str, hashed_password: str) -> Annie:
        """method to add farm user via email and hashd
password and saved to db"""
        try:
            dct = {}
            dct['email'] = email
            dct['hashed_password'] = hashed_password
            usr = Annie(**dct)

            usr.updated_at = datetime.utcnow()
            self.__session.add(usr)
            self.__session.commit()
            return usr
        except Exception:
            self.__session.rollback()
        return None

    def find_farm_user_by(self, **kwargs) -> Farm:
        """find a farm user by their email or entered keywrd"""
        fields, values = [], []
        for key, value in kwargs.items():
            if hasattr(Farm, key):
                fields.append(getattr(Farm, key))
                values.append(value)
            else:
                raise InvalidRequestError()
        result = self.__session.query(Farm).filter(
            tuple_(*fields).in_([tuple(values)])
        ).first()
        if result is None:
            raise NoResultFound()
        return result

    def find_buildex_user_by(self, **kwargs) -> Buildex:
        """find a user by their email or entered keywrd"""
        fields, values = [], []
        for key, value in kwargs.items():
            if hasattr(Buildex, key):
                fields.append(getattr(Buildex, key))
                values.append(value)
            else:
                raise InvalidRequestError()
        result = self.__session.query(Buildex).filter(
            tuple_(*fields).in_([tuple(values)])
        ).first()
        if result is None:
            raise NoResultFound()
        return result

    def find_solar_user_by(self, **kwargs) -> Solar:
        """find a solar user by their email or entered keywrd"""
        fields, values = [], []
        for key, value in kwargs.items():
            if hasattr(Solar, key):
                fields.append(getattr(Solar, key))
                values.append(value)
            else:
                raise InvalidRequestError()
        result = self.__session.query(Solar).filter(
            tuple_(*fields).in_([tuple(values)])
        ).first()
        if result is None:
            raise NoResultFound()
        return result

    def find_annie_user_by(self, **kwargs) -> Annie:
        """find a annie user by their email or entered keywrd"""
        fields, values = [], []
        for key, value in kwargs.items():
            if hasattr(Annie, key):
                fields.append(getattr(Annie, key))
                values.append(value)
            else:
                raise InvalidRequestError()
        result = self.__session.query(Annie).filter(
            tuple_(*fields).in_([tuple(values)])
        ).first()
        if result is None:
            raise NoResultFound()
        return result

    def update_farm_user(self, user_id: str, **kwargs) -> None:
        """method to update farm user"""
        """Updates a farm user based on a given id.
        """
        user = self.find_farm_user_by(id=user_id)
        if user is None:
            return
        update_source = {}
        for key, value in kwargs.items():
            if hasattr(Farm, key):
                update_source[getattr(Farm, key)] = value
            else:
                raise ValueError()
        self.__session.query(Farm).filter(Farm.id == user_id).update(
            update_source,
            synchronize_session=False,
        )
        self.__session.commit()

    def update_buildex_user(self, user_id: str, **kwargs) -> None:
        """method to update buildex user"""
        """Updates a buildex farm user based on a given id.
        """
        user = self.find_buildex_user_by(id=user_id)
        if user is None:
            return
        update_source = {}
        for key, value in kwargs.items():
            if hasattr(Buildex, key):
                update_source[getattr(Buildex, key)] = value
            else:
                raise ValueError()
        self.__session.query(Buildex).filter(Buildex.id == user_id).update(
            update_source,
            synchronize_session=False,
        )
        self.__session.commit()

    def update_solar_user(self, user_id: str, **kwargs) -> None:
        """method to update solar user"""
        """Updates a solar user based on a given id.
        """
        user = self.find_solar_user_by(id=user_id)
        if user is None:
            return
        update_source = {}
        for key, value in kwargs.items():
            if hasattr(Solar, key):
                update_source[getattr(Solar, key)] = value
            else:
                raise ValueError()
        self.__session.query(Farm).filter(Solar.id == user_id).update(
            update_source,
            synchronize_session=False,
        )
        self.__session.commit()

    def update_annie_user(self, user_id: str, **kwargs) -> None:
        """method to update farm user"""
        """Updates a farm user based on a given id.
        """
        user = self.find_farm_user_by(id=user_id)
        if user is None:
            return
        update_source = {}
        for key, value in kwargs.items():
            if hasattr(Farm, key):
                update_source[getattr(Farm, key)] = value
            else:
                raise ValueError()
        self.__session.query(Farm).filter(Farm.id == user_id).update(
            update_source,
            synchronize_session=False,
        )
        self.__session.commit()
