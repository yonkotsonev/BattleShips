from event_manager import EventManager
from random import randint
from position import Position

class Level1:
    def __init__(self, game):
        self.__eventManager = EventManager(game)
        self.__game = game
        self.__levelComplete = False
        self.__createdAsteroids = 0
    
    def run(self):
        while self.__levelComplete == False:
            self.__eventManager.PreProcess()
            for event in self.__game.GetEvents():
                self.__eventManager.ProcessEvent(event)
                
            self.__game.SetBackGround(self.__game.BLACK)
                
            self.GameLogic()
            self.__game.Draw()
            
            self.__game.RefreshScreen()
                
    def GameLogic(self):
        if randint(0,10000) % 17 == 0 and len(self.__game.GetAstroids()) < 10:
            self.__game.CreateAsteroid(Position(randint(0,800), 0))
            self.__createdAsteroids += 1
            
        self.__game.CheckForCollisions()
            
        for obj in self.__game.GetAstroids():
            obj.GoDown(2)
        
        for obj in self.__game.GetBullets():
            obj.GoUp()
            
        self.__game.ClearDeadObjects()
        
        if self.__createdAsteroids > 10000:
            self.__levelComplete = True