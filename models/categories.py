#!/usr/bin/python3
'''Categories Model
'''
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Text, Table, ForeignKey
from sqlalchemy.orm import relationship

image_categories = Table(
    "image_categories", Base.metadata,
    Column(
        "image_id",
        String(60),
        ForeignKey("images.id"),
        primary_key=True
    ),
    Column(
        "category_id",
        String(60),
        ForeignKey("categories.id"),
        primary_key=True
    )
)

Category.images = relationship(
    "Image", secondary=image_categories, back_populates="categories"
)


class Category(BaseModel, Base):
    '''A category class that inherits from BaseModel'''
    __tablename__ = "Categories"

    name = Column(
        String(255),
        nullable=False,
        unique=True
    )
    description = Column(
        Text
    )
