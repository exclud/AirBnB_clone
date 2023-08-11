#!/usr/bin/python3
"""Contains tests for the FileStorage Class"""

import unittest
from models.engine import file_storage
from models.base_model import BaseModel
import json


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage Class"""
    def test_all_function(self):
        """Tests for the all fuction that it returns the dictionary
        """
        storage = file_storage.FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        