from game_object import GameObject
from explosion import Explosion

class Ship(GameObject):
    def __init__(self, game):
        super(Ship, self).__init__('ship.png', game)
        self.health = 100
        
    def Hit(self, points):
        self.health -= points
        
        explosion = Explosion(self.game)
        explosion.rect.x = self.rect.x + explosion.rect.width/2
        explosion.rect.y = self.rect.y + explosion.rect.height / 2
        self.game.explosions.add(explosion)
        self.game.sprites.add(explosion)
        
    def GoRight(self, speed = 5):
        self.rect.x += speed
        
        if self.rect.x > self.game.WIDTH:
            self.rect.x = 0 - self.rect.width
        
    def GoLeft(self, speed = 5):
        self.rect.x -= speed
        
        if self.rect.x < 0 - self.rect.width:
            self.rect.x = self.game.WIDTH