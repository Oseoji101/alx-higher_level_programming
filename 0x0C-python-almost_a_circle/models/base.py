#!/usr/bin/python3
"""This module contains a class to serve as base for other classes"""


import csv
import json


class Base:
    """Represents base of all classes created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON representation of list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

       
       @classmethod
       def save_to_file(cls, list_objs):
           """writes the JSON string representation of list_objs to a file"""
           filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))


        @staticmethod
        def from_json_string(json_string):
            """returns the list of the JSON string representation"""
            if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string


        @classmethod
        def create(cls, **dictionary):
            """returns an instance with all attributes already set"""
            if cls.__name__ == 'Rectangle':
            egede = cls(1, 1)
        elif cls.__name__ == 'Square':
            egede = cls(1)

        egede.update(**dictionary)
        return egede


        @classmethod
        def load_from_file(cls):
            """returns a list of instances"""
            filename = str(cls.__name__) + ".json"

        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
