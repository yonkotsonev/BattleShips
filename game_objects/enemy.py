from game_object import GameObject
from random import randint

class Enemy(GameObject):
    def __init__(self, game):
        super(Enemy, self).__init__('enemy.png', game)

        self.rect.x = randint(0,self.game.WIDTH - self.rect.width)
        self.rect.y = 0
        
    def update(self, speed = 1):
        GameObject.update(self, speed)

        self.rect.y += speed
        if len(self.game.bullets) % 2 == 0 and randint(0,100) % 9 == 0 and self.rect.y % 2 == 0:
            self.game.Fire(self)
        else:
            offset = randint(1,3)
            self.rect.x = (self.rect.x + offset) % self.game.WIDTH
        if self.rect.y > self.game.HEIGHT:
            self.kill()
