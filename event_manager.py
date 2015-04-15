from pygame.locals import *

class EventManager(object):    
    def __init__(self, game):
        self.game = game
        self.lefKeyPressed = False
        self.rightKeyPressed = False
        
    def PreProcess(self):
        if self.lefKeyPressed:
            self.game.GoLeft()
            
        if self.rightKeyPressed:
            self.game.GoRight()
    
    def ProcessEvent(self, event):
        if event.type == QUIT:
            self.game.Quit();
            
        if event.type == KEYDOWN and event.key == K_LEFT:
            self.lefKeyPressed = True;
            
        if event.type == KEYUP and event.key == K_LEFT:
            self.lefKeyPressed = False;
            
        if event.type == KEYDOWN and event.key == K_RIGHT:
            self.rightKeyPressed = True;
            
        if event.type == KEYUP and event.key == K_RIGHT:
            self.rightKeyPressed = False;
            
        if event.type == KEYDOWN and event.key == K_SPACE:
            self.game.PlaySound(self.game.fireSound)
            self.game.Fire()
            
        if event.type == KEYDOWN and event.key == K_F2:
            self.game.Restart()
        
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            self.game.Quit();