#!/usr/bin/python3
"""Class Base"""


import json


class Base():
    """ private class attribute __nb_objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Builder"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
             That returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
            That writes the JSON string representation of
            list_objs to a file:
        """

        filename = cls.__name__ + '.json'
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None or list_objs == []:
                file.write([])
            else:
                list_dic = []
                for dic in list_objs:
                    list_dic += [(dic.to_dictionary())]
                dic_l = Base.to_json_string(list_dic)
                file.write(dic_l)

    @staticmethod
    def from_json_string(json_string):
        """
            that returns the list of the JSON string
            representation json_string:
            -json_string is a string representing a list of dictionaries
            -If json_string is None or empty, return an empty list
            -Otherwise, return the list represented by json_string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
           That returns an instance with all attributes already set:
        """
        if cls.__name__ == "Rectangle":
            obj_j = cls(4, 5)
        else:
            obj_j = cls(6)
        obj_j.update(**dictionary)
        return(obj_j)

    @classmethod
    def load_from_file(cls):
        """That returns a list of instances:"""
        filename = cls.__name__ + '.json'

        try:
            list_ins = []
            with open(filename, encoding="utf-8") as file:
                dic = Base.from_json_string(file.read())
                for item in dic:
                    list_ins += [cls.create(**item)]
                return list_ins
        except:
            return []
