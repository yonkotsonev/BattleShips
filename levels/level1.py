from random import randint

class Level1:
    def __init__(self, game):
        self.game = game
        self.levelComplete = False
        self.createdAsteroids = 0
                
    def GameLogic(self):
        if randint(0,10000) % 17 == 0 and len(self.game.asteroids) < 10:
            self.game.CreateAsteroid((randint(0,800), 0))
            self.createdAsteroids += 1

        if self.createdAsteroids > 10000:
            self.levelComplete = True