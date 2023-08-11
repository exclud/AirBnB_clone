#!/usr/bin/python3
"""Contains the review class"""

import models
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialization of Review attributes"""
        super().__init__(*args, **kwargs)
