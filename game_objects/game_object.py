'''
Created on Apr 6, 2015

@author: ytsonev
'''

from position import Position

class GameObject(object):
    '''
    Parent class for all game object classes
    '''
    WIDTH = 0
    HEIGHT = 0
    IMAGE = None

    def __init__(self, position):
        '''
        Constructor
        '''
        assert isinstance(position, Position)
        
        self.__position = position
        self.__isAlive = True
        
    def Position(self, position = None):
        if position is None:
            return self.__position
        
        assert isinstance(position, Position)
        self.__position = position
        
    def Draw(self, game):
        game.DrawImage(self.IMAGE, self.__position)
    
    def CheckForCollision(self, obj):
        assert isinstance(obj, GameObject)
        if (self.Position().X() < obj.Position().X() + obj.WIDTH  and self.Position().X() + self.WIDTH  > obj.Position().X() and
            self.Position().Y() < obj.Position().Y() + obj.HEIGHT and self.Position().Y() + self.HEIGHT > obj.Position().Y()):
            
            return True
        
        return False
    
    def IsAlive(self):
        return self.__isAlive
    
    def Kill(self):
        self.__isAlive = False
        
    def GoRight(self, speed = 5):
        newX = self.__position.X() + speed
        
        if newX > 800:
            newX = 0 - self.WIDTH
            
        self.__position.X(newX)
        
    def GoLeft(self, speed = 5):
        newX = self.__position.X() - speed
        
        if newX < 0 - self.WIDTH:
            newX = 800
            
        self.__position.X(newX)
        
    def GoDown(self, speed = 5):
        newY = self.__position.Y() + speed
        
        if newY > 600:
            self.__isAlive = False
            
        self.__position.Y(newY)
        
    def GoUp(self, speed = 5):
        newY = self.__position.Y() - speed
        
        if newY < 0:
            self.__isAlive = False
            
        self.__position.Y(newY)