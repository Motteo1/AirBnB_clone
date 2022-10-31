#!/usr/bin/python3
"""Class FileStorage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Class that serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {} #empty dictionary

    def all(self):
        """Returns the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the 'obj' with key '<obj class name>.id'"""
        if obj:
            FileStorage.__objects[type(obj).__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes '__objects' to the JSON file '__file_path'"""
        temp = FileStorage.__objects
        new_dct = {obj: temp[obj].to_dict() for obj in temp.keys()}
        with open(FileStorage.__file_path, 'w') as jf:
            json.dump(new_dct, jf)

    def reload(self):
        """Deserializes the JSON file to '__objects' on condition
        that the JSON file exists, else, does nothing
        """
        try:
            with open(FileStorage.__file_path, 'r') as po:
                FileStorage.__objects = json.load(po)
                if self.__objects:
                    for key, val in FileStorage.__objects.items():
                        class_name = val['__class__']
                        class_name = models.classes[class_name]
                        FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
