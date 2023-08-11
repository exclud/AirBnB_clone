#!/usr/bin/python3
"""Contains the amenity class"""

import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity which inherits from the BaseModel Class

    Args:
        BaseModel (_type_): _description_
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of Amenity
        """
        super().__init__(*args, **kwargs)
