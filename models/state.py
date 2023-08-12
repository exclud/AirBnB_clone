#!/usr/bin/python3
"""Contains the state class"""

import models
from models.base_model import BaseModel


class State(BaseModel):
    """The class State which inherits from BaseModel class

    Args:
        BaseModel (_type_): The main class which is being inherited from
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initialization of the State Class"""
        super().__init__(*args, **kwargs)
