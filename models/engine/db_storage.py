#!/usr/bin/python3

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.categories import Category
from models.images import Image
from models.photographers import Photographer
from os import getenv


class DBStorage:
    """
    Database storage engine
    """
    __engine = None
    __session = None
    __classes = [Photographer]  # add rest of models after test success

    def __init__(self) -> None:
        """Instantiate the storage model"""
        db_url = (
            f"mysql+mysqldb:{getenv('BMP_MYSQL_USER')}:"
            f"{getenv('BMP_MYSQL_PWD')}@{getenv('BMP_MYSQL_HOST')}/"
            f"{getenv('BMP_MYSQL_DB')}"
        )
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        # drop tables if environment is a test environ
        if getenv('BMP_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    # Define a method that creates all tables mapped by the models in the
    # database, if they do not already exist. Setup a factory session
    # bound to the engine and initialise a session to ensure each thread
    # has its own session
    def reload(self):
        """Create all tables mapped by the metadata in
        Base (declarative base)
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()

    # Define a method to return all objects of a given class if class name
    # is specified or all objects if no class name is specified
    def all(self, cls=None):
        """
        This method queries all objects in the current database session
        if no class name is specified and queries all objects of a given
        class if the class name is specified
        """
        objects = {}
        if cls:
            for obj in self.__session.query(cls):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for clss in self.__classes:
                for obj in self.__session.query(clss):
                    objects[obj.__class__.__name__ + '.' + obj.id] = obj

        return objects

    # Define a method that creates a new object by adding it to the
    # current database session
    def new(self, obj):
        """
        This method adds a new object to the current databases session
        """
        self.__session.add(obj)

    # Define a method that saves (commits) changes to the database session
    def save(self):
        """
        This method commits changes to the database session
        """
        self.__session.commit()

    # Define a method that deletes an object from the database session
    def delete(self, obj=None):
        """
        This method deletes an object from the database session if the
        object is specified.
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    # Define a method to close the current database session
    def close(self):
        """Closes the current database session"""
        self.__session.close()

    # Define a method to retrive an object based on an id
    def get(self, cls, id):
        """Retrieves an object based on the id given"""
        return self.__session.query(cls).get(id)

    # Define a method to count the number of object instances in the
    # database
    def count(self, cls=None):
        """
        Counts the number of instances of an object"""
        if cls:
            return self.__session.query(cls).count()
        else:
            for clss in self.__classes:
                count += self.__session.query(clss).count()
            return count
