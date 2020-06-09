#!/usr/bin/python3
"""Class Base"""


import json
import csv


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
            return "[]"
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
            if list_objs is None:
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method thats deserializes in CSV"""
        csvfile = '{}.csv'.format(cls.__name__)
        with open(csvfile, mode="w", newline='') as csvf:
            if list_objs is None or list_objs == []:
                csvf.write('[]')
            else:
                if cls.__name__ == 'Square':
                    attr = ["id", "size", "x", "y"]
                else:
                    attr = ["id", "width", "height", "x", "y"]
                doc = csv.DictWriter(csvf, fieldnames=attr)
                list_csv = []
                for inst in list_objs:
                    list_csv += [doc.writerow(inst.to_dictionary())]

    @classmethod
    def load_from_file_csv(cls):
        """Method thats deserializes in CSV"""
        csvfile = '{}.csv'.format(cls.__name__)
        try:
            with open(csvfile, mode="r", newline='') as csvf:
                if cls.__name__ == 'Square':
                    attr = ["id", "size", "x", "y"]
                else:
                    attr = ["id", "width", "height", "x", "y"]
                doc = csv.DictReader(csvf, fieldnames=attr)
                csv_dics = [{key: int(value) for key, value in dic.items()}
                            for dic in doc]
                return [cls.create(**dics) for dics in csv_dics]
        except IOError:
            return []
