#!/usr/bin/python3
'''UserModel module
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''A user model that inherits from BaseModel'''
    user_id = ''
    user_name = ''
    email = ''
    password = ''
    profile = ''
