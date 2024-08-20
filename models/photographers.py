#!/usr/bin/python3
'''Photographers Model
'''
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Text
from sqlalchemy.orm import relationship


class Photographer(BaseModel, Base):
    '''A Photographer model that inherits from BaseModel'''
    __tablename__ = "Photographers"

    name = Column(
        String(255),
        nullable=False
    )
    bio = Column(
        Text
    )
    email = Column(
        String(255),
        nullable=False,
        unique=True
    )
    phone = Column(
        String(20)
    )

    images = relationship(
        "Image", back_populates="photographer"
    )
