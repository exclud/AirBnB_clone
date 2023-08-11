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

    def test_init_with_kwargs(self):
        """Test __init__ method with keyword arguments"""
        data = {
            'id': '123',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-01T13:00:00.000000',
            'custom_attr': 'test'
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, '123')
        self.assertEqual(model.custom_attr, 'test')
        self.assertEqual(model.created_at, datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(model.updated_at, datetime(2023, 1, 1, 13, 0, 0))

    def test_init_without_kwargs(self):
        """Test __init__ method without keyword arguments"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in model_dict)
        self.assertTrue()
