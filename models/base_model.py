#!/usr/bin/python3
'''BaseModel module for BMP Studio
'''
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel():
    '''BaseModel class that defines all common attributes/methods
    for other classes.
    '''
    id = Column(
        String(60),
        nullable=False,
        primary_key=True
    )
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.now()
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.now()
    )

    def __init__(self, **kwargs) -> None:
        '''An instance of PhotoModel class

        Args:
            **kwargs (any): key-worded arguments
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'
                        )
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self) -> str:
        '''Returns a string representation of class.name, id and dict'''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self) -> None:
        '''Updates the public instance attr updated_at with the current
        datetime
        '''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self) -> dict:
        '''Returns a dictionary containing all keys/values of __dict__
        of an instance
        '''
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
