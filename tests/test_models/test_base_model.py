#!/usr/bin/python3
"""Tests for the BaseModel class from test_bast_model.py"""


from datetime import datetime
import unittest
import time
import models
BaseModel = models.base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel Class"""
    
    def test_str(self):
        """Tests for the __str__ function to check if the outputs are correct
        """
        model = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_output)

    def test_save(self):
        """Tests for the save function that it updates to the current time
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    