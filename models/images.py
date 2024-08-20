#!/usr/bin/python3
'''Images Model
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship


class Image(BaseModel, Base):
    '''Image class that inherits from BaseModel'''
    __tablename__ = "Images"

    title = Column(
        String(255),
        nullable=False
    )
    description = Column(
        Text
    )
    url = Column(
        String(255),
        nullable=False
    )
    photographer_id = Column(
        String(60),
        ForeignKey("Photographers.id")
    )

    photographer = relationship(
        "Photographer", back_populates="images"
    )
    categories = relationship(
        "Category", secondary="Image_Categories", back_populates="images"
    )
