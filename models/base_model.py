#!usr/bin/python3
"""
Class 'BaseModel'
parent class
"""
from uuid import uuid4
from datetime import datetime


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
                    self.created_at = datetime.strtime(kwargs["created_at"],
                                                        "isoformat()")
                elif "updated_at" == key:
                    self.updated_at = datetime.strtime(kwargs["created_at"],
                                                        "isoformat()")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
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
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
