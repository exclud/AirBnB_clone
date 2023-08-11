#!/usr/bin/python3
"""Contains the user class"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """Class User that inherits from BaseModel

    Args:
        BaseModel (_type_): Class BaseModel
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """Initialization of the public atributes
        """
        super().__init__(*args, **kwargs)
