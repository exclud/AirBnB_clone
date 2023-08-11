#!/usr/bin/python3
"""Contains the FileStorage Class"""

from models.amenity import Amenity
from models.city import City
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os.path import exists
import json

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to instances

    Returns:
        private attributes: serialization instances
    """
    __file_path = "file.json"
    # String to path to the JSON file (file.json)
    __objects = {}
    #  dictionary - empty but will store all objects by <class name>.id

    def all(self):
        """Function which returns the dictionary __objects

        Returns:
            __objects: Dictionary objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            obj (_type_): Key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
