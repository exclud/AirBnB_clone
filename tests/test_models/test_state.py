#!/usr/bin/python3
"""Tests for the State Class
Functionalities testsed: inheritance, attribute existence,
attribute values, and initialization
"""

import models
import unittest
from models import state
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests for the State class"""

    def test_state_inherits_base_model(self):
        """Test if State class inherits from BaseModel"""
        self.assertTrue(issubclass(state.State, BaseModel))

    def test_state_name_attribute_exists(self):
        """Test if State class has a name attribute"""
        new_state = state.State()
        self.assertTrue(hasattr(new_state, 'name'))

    def test_state_name_attribute_is_empty_string(self):
        """Test if State class name attribute is
        initialized as an empty string"""
        new_state = state.State()
        self.assertEqual(new_state.name, '')

    def test_state_init_inherits_base_model_init(self):
        """Test if State class __init__ inherits from BaseModel __init__"""
        new_state = state.State()
        self.assertTrue(hasattr(new_state, 'id'))
        self.assertTrue(hasattr(new_state, 'created_at'))
        self.assertTrue(hasattr(new_state, 'updated_at'))
