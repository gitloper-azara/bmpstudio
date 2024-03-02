#!/usr/bin/python3
'''TagModel module
'''
from models.base_model import BaseModel


class Tag(BaseModel):
    '''A tag class that inherits from BaseModel'''
    tag_id = ''
    tag_name = ''
    photo_id = []
