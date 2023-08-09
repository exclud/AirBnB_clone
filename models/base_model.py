#!/usr/bin/python3

"""Class Base Model"""

import models

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    
    def __str__(self):
        """String Representation of the BaseModel Class

        Returns:
            str: Prints [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)
