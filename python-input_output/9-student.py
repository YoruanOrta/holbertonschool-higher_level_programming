#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that retrieves a dictionary representation"""
        return self.__dict__
