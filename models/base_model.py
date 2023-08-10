#!/usr/bin/python3

"""Class Base Model"""

import models
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The BaseModel Class from which other classes are derived.
    """

    def __init__(self, *args, **kwargs):
        """Initialization of the attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            
        # unique identifier for each instance
            # self.created_at = self.updated_at = datetime.now
        # assigns the current datetime when a new instance is created.
            # self.updated_at = datetime.now()
        # assign the current time and update it when an object is changed.

    def __str__(self):
        """String Representation of the BaseModel Class

        Returns:
            str: Prints [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """The function updates the update_at instance with the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert instance attributes to a dictionary

        Returns:
            obj_dict: Dictionary representation
        """
        obj_dict = self.__dict__.copy()
        if "created_at" in obj_dict:
            obj_dict["created_at"] = obj_dict["created_at"].strftime(time)
        if "updated_at" in obj_dict:
            obj_dict["updated_at"] = obj_dict["updated_at"].strftime(time)
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
