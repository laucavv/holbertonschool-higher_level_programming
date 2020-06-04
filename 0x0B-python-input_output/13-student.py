#!/usr/bin/python3
""" class Student """


class Student:
    def __init__(self, first_name, last_name, age):
        "builder"
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            method that retrieves a dictionary representation
            of a Student instance
        """
        if attr is None:
            return self.__dict__

        my_dic = {}

        for elements in attr:
            if elements in self.__dict__:
                my_dic[elements] = self.__dict__[elements]

        return my_dic

    def reload_from_json(self, json):
        """
            method that replaces all attributes of
            the Student instance
        """
        for key, value in json.items():
            self.__dict__[key] = value
