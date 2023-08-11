#!/usr/bin/python3
"""Class City which inherits from BaseModel"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """Class City which inherits from the BaseModel Class

    Args:
        BaseModel (_type_): _description_
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the city class
        """
        super().__init__(*args, **kwargs)
