#!/usr/bin/python3
'''Creates a uniq instance of the storage model
to handle data recovery on session restart
'''
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

storage_t = os.getenv('BMP_TYPE_STORAGE')

if storage_t == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
