'''
Created on Apr 6, 2015

@author: ytsonev
'''
from __builtin__ import int

class Position(object):
    '''
    Class for the position objects
    '''


    def __init__(self, x, y):
        '''
        Constructor
        '''
        assert isinstance(x, int)
        assert isinstance(y, int)
        
        self.__x = x
        self.__y = y
        
    def X(self, x = None):
        if x is None:
            return self.__x
        
        assert isinstance(x, int)
        
        self.__x = x
        
    def Y(self, y = None):
        if y is None:
            return self.__y
        
        assert isinstance(y, int)
        
        self.__y = y
        
    def ToTuple(self):
        return (self.__x, self.__y)