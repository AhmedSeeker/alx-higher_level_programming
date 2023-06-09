#!/usr/bin/python3
'''class MagicClass: definition of class
    that do the same as a given python bytecode
'''

from math import pi


class MagicClass:
    ''' Definition of class MagicClass
    '''

    def __init__(self, radius=0):
        ''' Initialises current instance
        '''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        ''' Returns area of current instance
        '''
        return (self.__radius ** 2) * pi

    def circumference(self):
        ''' Returns the circumference of current instance
        '''
        return 2 * pi * self.__radius
