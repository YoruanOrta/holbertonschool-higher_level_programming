#!/usr/bin/python3
"""Module for Student class."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Instantiation method."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that retrieves a dictionary
        representation of a Student instance."""
        return self.__dict__

    def reload_from_json(self, json):
        """Method that replaces all attributes of the Student instance."""
        for key in json:
            setattr(self, key, json[key])

    def __str__(self):
        """Method that retrieves a string
        representation of a Student instance."""
        return "[Student] {} {} {}".format(
                    self.first_name, self.last_name, self.age
                    )
