#!/usr/bin/python3
'''A command line interpreter that performs CRUD operations
for the website.
'''

import cmd
import shlex
from models.album import Album
from models.base_model import BaseModel
from models.photo import Photo
from models.review import Review
from models.tags import Tag
from models.user import User
from models import storage


class BMPCommand(cmd.Cmd):
    '''Console that performs CRUD operations.'''
    prompt = '(bmp )'
    methods = {
        'BaseModel': BaseModel,
        'Album': Album,
        'Photo': Photo,
        'Review': Review,
        'Tag': Tag,
        'User': User
    }

def parse(line):
    '''Handles command line parsing using shell logic.'''
    return shlex.split(line)


if '__name__' == '__main__':
    BMPCommand().cmdloop()
