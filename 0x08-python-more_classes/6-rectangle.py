#!/usr/bin/python3
''' Module: Creates class Rectangle
'''


class Rectangle:
    ''' Defines a Rectangle class
    '''
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        ''' Initialize instance
        '''
        self.height = height
        self.width = width
        number_of_instances += 1

    @property
    def width(self):
        ''' Gets width value
        '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Sets width
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' Gets height value
        '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Sets height
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' Gets rectangle area
        '''
        return self.width * self.height

    def perimeter(self):
        ''' Gets rectanlge perimeter
        '''
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        ''' Gets string representation
        '''
        if self.width == 0 or self.height == 0:
            return ''
        return ('\n'.join(['#' * self.width] * self.height))

    def __repr__(self):
        if self.width == 0 or self.height == 0:
            return ''
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        ''' Deletes the current instance
        '''
        number_of_instances -= 1
        print('Bye rectangle...')
