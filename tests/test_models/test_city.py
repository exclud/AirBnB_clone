#!/usr/bin/python3
"""Tests for the City Clas
They cover functionality: inheritance, attributes and initalization
"""

import models
from models import city
from models.base_model import BaseModel
import unittest


class TestCity(unittest.TestCase):
    """Tests for the City Class"""

    def test_city_inherits_base_model(self):
        """Test if City class inherits from BaseModel"""
        self.assertTrue(issubclass(city.City, BaseModel))

    def test_city_attributes_exist(self):
        """Test if City class attributes exist"""
        new_city = city.City()
        self.assertTrue(hasattr(new_city, 'state_id'))
        self.assertTrue(hasattr(new_city, 'name'))

    def test_city_attributes_are_empty_strings(self):
        """Test if City class attributes are initialized as empty strings"""
        new_city = city.City()
        self.assertEqual(new_city.state_id, '')
        self.assertEqual(new_city.name, '')

    def test_city_init_inherits_base_model_init(self):
        """Test if City class __init__ inherits from BaseModel __init__"""
        new_city = city.City()
        self.assertTrue(hasattr(new_city, 'id'))
        self.assertTrue(hasattr(new_city, 'created_at'))
        self.assertTrue(hasattr(new_city, 'updated_at'))
