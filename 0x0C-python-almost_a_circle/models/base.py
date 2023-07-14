#!/usr/bin/python3
''' Module for Base class
'''


class Base:
    ''' Representing Base class '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Initialize instance '''
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects