from game_object import GameObject
from random import randint

class Asteroid(GameObject):
    def __init__(self, game):
        super(Asteroid, self).__init__('asteroid.png', game)
        
        self.rect.x = randint(0,self.game.WIDTH - self.rect.width)
        self.rect.y = 0
        
    def update(self, speed = 2):
        GameObject.update(self, speed)

        self.rect.y += speed
        if self.rect.y > self.game.HEIGHT:
            self.kill()