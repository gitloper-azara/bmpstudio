#!/usr/bin/python3
'''AlbumModel module
'''
from models.base_model import BaseModel


class Album(BaseModel):
    '''An album class that inherits from BaseModel'''
    album_id = ''
    title = ''
    description = ''
    cover_id = ''
    photo_id = []
