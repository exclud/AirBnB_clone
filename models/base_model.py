#!/usr/bin/python3

"""Class Base Model"""

import models
import uuid
import datetime as datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The BaseModel Class from which other classes are derived.
    """

    def __init__(self):
        """Initialization of the attributes
        """
        self.id = str(uuid.uuid4())
        # unique identifier for each instance
        self.created_at = datetime.now()
        # assigns the current datetime when a new instance is created.
        self.updated_at = datetime.now()
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
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
