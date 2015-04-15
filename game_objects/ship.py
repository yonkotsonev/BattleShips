from game_object import GameObject

class Ship(GameObject):
    def __init__(self, game):
        super(Ship, self).__init__('ship.png', game)
        self.health = 100
        
    def GoRight(self, speed = 5):
        self.rect.x += speed
        
        if self.rect.x > self.game.WIDTH:
            self.rect.x = 0 - self.rect.width
        
    def GoLeft(self, speed = 5):
        self.rect.x -= speed
        
        if self.rect.x < 0 - self.rect.width:
            self.rect.x = self.game.WIDTH