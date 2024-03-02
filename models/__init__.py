#!/usr/bin/python3
'''Creates a uniq instance of the storage model
to handle data recovery on session restart
'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
