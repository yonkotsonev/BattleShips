from random import randint
import pygame

class Level1:
    def __init__(self, game):
        self.game = game
        self.levelComplete = False
        self.createdAsteroids = 0
        self.background = pygame.image.load('images/level_1_bg.jpg').convert()
        self.bonus = 0
        self.targetScore = 1250
                
    def GameLogic(self):
        if randint(0,10000) % 17 == 0 and len(self.game.asteroids) < 10:
            self.game.CreateAsteroid()
            self.createdAsteroids += 1

        if self.createdAsteroids > 500: 
            if self.game.score > self.targetScore:
                self.levelComplete = True
                self.bonus = self.game.score - self.targetScore
            else:
                self.game.player.kill()
                
    def __str__(self):
        return 'LEVEL 1'