#!/usr/bin/python3
"""Test for the Place class
Functionalities tested: attributes, inheritance and instantation
"""

import models
from models import place
from models.base_model import BaseModel
import unittest


class TestPlace(unittest.TestCase):
    """Test for the Place class"""

    def test_place_inherits_base_model(self):
        """Test if Place class inherits from BaseModel"""
        self.assertTrue(issubclass(place.Place, BaseModel))

    def test_place_attributes_exist(self):
        """Test if Place class attributes exist"""
        new_place = place.Place()
        self.assertTrue(hasattr(new_place, 'city_id'))
        self.assertTrue(hasattr(new_place, 'user_id'))
        self.assertTrue(hasattr(new_place, 'name'))
        self.assertTrue(hasattr(new_place, 'description'))
        self.assertTrue(hasattr(new_place, 'number_rooms'))
        self.assertTrue(hasattr(new_place, 'number_bathrooms'))
        self.assertTrue(hasattr(new_place, 'max_guest'))
        self.assertTrue(hasattr(new_place, 'price_by_night'))
        self.assertTrue(hasattr(new_place, 'latitude'))
        self.assertTrue(hasattr(new_place, 'longitude'))
        self.assertTrue(hasattr(new_place, 'amenity_ids'))

    def test_place_attributes_defaults(self):
        """Test if Place class attributes have default values"""
        new_place = place.Place()
        self.assertEqual(new_place.city_id, "")
        self.assertEqual(new_place.user_id, "")
        self.assertEqual(new_place.name, "")
        self.assertEqual(new_place.description, "")
        self.assertEqual(new_place.number_rooms, 0)
        self.assertEqual(new_place.number_bathrooms, 0)
        self.assertEqual(new_place.max_guest, 0)
        self.assertEqual(new_place.price_by_night, 0)
        self.assertEqual(new_place.latitude, 0.0)
        self.assertEqual(new_place.longitude, 0.0)
        self.assertEqual(new_place.amenity_ids, [])

    def test_place_init_inherits_base_model_init(self):
        """Test if Place class __init__ inherits from BaseModel __init__"""
        new_place = place.Place()
        self.assertTrue(hasattr(new_place, 'id'))
        self.assertTrue(hasattr(new_place, 'created_at'))
        self.assertTrue(hasattr(new_place, 'updated_at'))
