#!/usr/bin/env python3
class Base:
    """ Represents the base model for all other classes
        Attributes:
            __nb_objects(int): number of instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise new Base

            Args
                id(int): The identity of the new instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
