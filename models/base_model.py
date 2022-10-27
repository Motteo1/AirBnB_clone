#!usr/bin/python3
"""Class 'BaseModel', parent class
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for AirBnB project"""
    def __init__(self, *args, **kwargs):
        """Initialization method: UUID"""
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """Returns string info about the BaseModel"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """Stores the instance created"""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of an instance"""
        self.__dict__['__class__'] = self.__class__.__name__
        return (self.__dict__)
