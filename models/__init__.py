#!/usr/bin/python3
"""Initialize the BaseModel class and the FileStorage Class """


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
