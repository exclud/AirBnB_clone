#!/usr/bin/python3
"""Contains tests for the user class"""

import unittest
import models
from models.base_model import BaseModel
from models import user


class TestUser(unittest.TestCase):
    def test_user_init_inherits_base_model_init(self):
        """Test if User class __init__ inherits from BaseModel __init__"""
        new_user = user.User()
        self.assertTrue(hasattr(new_user, 'id'))
        self.assertTrue(hasattr(new_user, 'created_at'))
        self.assertTrue(hasattr(new_user, 'updated_at'))

    def test_user_attributes_are_empty_strings(self):
        """Test if User class attributes are initialized as empty strings"""
        new_user = user.User()
        self.assertEqual(new_user.email, '')
        self.assertEqual(new_user.password, '')
        self.assertEqual(new_user.first_name, '')
        self.assertEqual(new_user.last_name, '')

    def test_user_inherits_base_model(self):
        """Test if User class inherits from BaseModel"""
        self.assertTrue(issubclass(user.User, BaseModel))

    def test_user_attributes_exist(self):
        """Test if User class attributes exist"""
        new_user = user.User()
        self.assertTrue(hasattr(new_user, 'email'))
        self.assertTrue(hasattr(new_user, 'password'))
        self.assertTrue(hasattr(new_user, 'first_name'))
        self.assertTrue(hasattr(new_user, 'last_name'))
