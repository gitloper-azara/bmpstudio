#!/usr/bin/python3
'''ReviewModel module
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''A review class that inherits from BaseModel'''
    user_id = ''
    review_date = ''
    photo_id = ''
    rating = ''
    text = ''
