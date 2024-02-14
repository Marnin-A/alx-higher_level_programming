#!/usr/bin/python3
"""Define a base model class."""
import json
import csv
import turtle


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): a unique identifier for the class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
