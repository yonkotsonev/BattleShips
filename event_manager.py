from pygame.locals import *

class EventManager(object):    
    def __init__(self, game):
        self.__game = game
        self.__lefKeyPressed = False
        self.__rightKeyPressed = False
        
    def PreProcess(self):
        if self.__lefKeyPressed:
            self.__game.GoLeft()
            
        if self.__rightKeyPressed:
            self.__game.GoRight()
    
    def ProcessEvent(self, event):
        if event.type == QUIT:
            self.__game.Quit();
            
        if event.type == KEYDOWN and event.key == K_LEFT:
            self.__lefKeyPressed = True;
            
        if event.type == KEYUP and event.key == K_LEFT:
            self.__lefKeyPressed = False;
            
        if event.type == KEYDOWN and event.key == K_RIGHT:
            self.__rightKeyPressed = True;
            
        if event.type == KEYUP and event.key == K_RIGHT:
            self.__rightKeyPressed = False;
            
        if event.type == KEYDOWN and event.key == K_SPACE:
            self.__game.Fire()
            
        if event.type == KEYDOWN and event.key == K_F2:
            self.__game.Restart()
        
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            self.__game.Quit();