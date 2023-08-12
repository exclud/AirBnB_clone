#!/usr/bin/python3
"""
Contains the Tests for the Amenity Class
"""

import models
from models import amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity Class"""
    def test_inheritance(self):
        amenity = TestAmenity