from game_object import GameObject

class Asteroid(GameObject):
    def __init__(self, game):
        super(Asteroid, self).__init__('asteroid.png', game)
        
    def update(self, speed = 2):
        GameObject.update(self, speed)

        self.rect.y += speed
        if self.rect.y > self.game.HEIGHT:
            self.kill()