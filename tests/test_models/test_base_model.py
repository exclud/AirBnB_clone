#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

"""Tests for the BaseModel Class"""
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))


class TestBaseModel(unittest.TestCase):
    """Test The BaseModel Class"""
    def test_string(self):
        """Test the output of the str method.
        """
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))
