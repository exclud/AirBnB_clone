#!/usr/bin/python3
"""
Contains the Tests for the Amenity Class
The tests cover functionality of the Amenity class including
Inheritance, attribute test, initialization and attr val.
"""

import models
from models import amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity Class"""

    def test_amenity_inherits_base_model(self):
        """Test if Amenity class inherits from BaseModel"""
        self.assertTrue(issubclass(amenity.Amenity, BaseModel))

    def test_amenity_name_attribute_exists(self):
        """Test if Amenity class has a name attribute"""
        new_amenity = amenity.Amenity()
        self.assertTrue(hasattr(new_amenity, 'name'))

    def test_name_attribute_is_an_empty_string(self):
        """Test if Amenity class name attribute is
        initialized as an empty string"""
        new_amenity = amenity.Amenity()
        self.assertEqual(new_amenity.name, '')

    def test_amenity_init_inherits_base_model_init(self):
        """Test if Amenity class __init__ inherits from BaseModel __init__"""
        new_amenity = amenity.Amenity()
        self.assertTrue(hasattr(new_amenity, 'id'))
        self.assertTrue(hasattr(new_amenity, 'created_at'))
        self.assertTrue(hasattr(new_amenity, 'updated_at'))
