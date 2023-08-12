#!/usr/bin/python3
"""Tests for the Review class
Functionalities testsed: inheritance, attribute existence,
attribute values, and initialization
"""

import models
import unittest
from models import review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Tests for the Review class"""

    def test_review_inherits_base_model(self):
        """Test if Review class inherits from BaseModel"""
        self.assertTrue(issubclass(review.Review, BaseModel))

    def test_review_attributes_exist(self):
        """Test if Review class attributes exist"""
        new_review = review.Review()
        self.assertTrue(hasattr(new_review, 'place_id'))
        self.assertTrue(hasattr(new_review, 'user_id'))
        self.assertTrue(hasattr(new_review, 'text'))

    def test_review_attributes_are_empty_strings(self):
        """Test if Review class attributes are initialized as empty strings"""
        new_review = review.Review()
        self.assertEqual(new_review.place_id, '')
        self.assertEqual(new_review.user_id, '')
        self.assertEqual(new_review.text, '')

    def test_review_init_inherits_base_model_init(self):
        """Test if Review class __init__ inherits from BaseModel __init__"""
        new_review = review.Review()
        self.assertTrue(hasattr(new_review, 'id'))
        self.assertTrue(hasattr(new_review, 'created_at'))
        self.assertTrue(hasattr(new_review, 'updated_at'))
