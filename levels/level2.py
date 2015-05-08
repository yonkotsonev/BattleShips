from random import randint
import pygame

class Level2:
    def __init__(self, game):
        self.game = game
        self.levelComplete = False
        self.createdAsteroids = 0
        self.createdEnemies = 0
        self.background = pygame.image.load('images/level_2_bg.jpg').convert()
        self.bonus = 0
        self.targetScore = 2500
                
    def GameLogic(self):
        if randint(0,10000) % 17 == 0 and len(self.game.asteroids) < 5:
            self.game.CreateAsteroid()
            self.createdAsteroids += 1

        if randint(0,10000) % 19 == 0 and len(self.game.enemies) < 3:
            self.game.CreateEnemy()
            self.createdEnemies += 1

        if self.createdAsteroids + self.createdEnemies > 500: 
            if self.game.score > self.targetScore:
                self.levelComplete = True
                self.bonus = self.game.score - self.targetScore
            else:
                self.game.player.kill()
                
    def __str__(self):
        return 'LEVEL 2'
