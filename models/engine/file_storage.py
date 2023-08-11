#!/usr/bin/python3
"""Contains the FileStorage Class"""

from models.base_model import BaseModel
from models.user import User
import json


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

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)
            
    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    if class_name == 'BaseModel':
                        obj = BaseModel(**value)
                    elif class_name == 'User':
                        obj = User(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
