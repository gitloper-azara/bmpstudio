#!/usr/bin/python3
'''PhotoModel module
'''
from models.base_model import BaseModel


class Photo(BaseModel):
    '''Photo class that inherits from BaseModel'''
    photo_id = ''
    photographer = ''
    date_taken = ''
    description = ''
    tag = ''
