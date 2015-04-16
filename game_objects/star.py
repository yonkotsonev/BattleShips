from game_object import GameObject
from random import randint

class Star(GameObject):
    def __init__(self, game, time = 5):
        super(Star, self).__init__('star1.png', game)
        self.rect.x = randint(0, self.game.WIDTH - self.rect.width)
        self.rect.y = randint(0, self.game.HEIGHT - self.rect.height)
       
    def update(self, *args):
        GameObject.update(self, *args)

        self.rect.y += 3
        if self.rect.y > self.game.HEIGHT:
            self.kill()
            self.game.CreateStar()