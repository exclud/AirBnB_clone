#!/usr/bin/python3
"""Contains the Place class"""

import models
from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place that inherits from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialization of Place attributes"""
        super().__init__(*args, **kwargs)
