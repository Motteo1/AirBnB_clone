#!usr/bin/python3
"""
Class 'BaseModel'
parent class
"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Base class for AirBnB project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """Initialization method: UUID"""
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs[key],
                            "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs[key],
                            "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()
            models.storage.new(self)

    def __str__(self):
        """Returns string info about the BaseModel"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """Stores the instance created"""
        self.updated_at = datetime.now().isoformat()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of an instance"""
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
