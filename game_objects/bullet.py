from game_object import GameObject

class Bullet(GameObject):
    def __init__(self, game, enemy = False):
        super(Bullet, self).__init__('bullet.png', game)
        self.enemy = enemy

        
    def update(self, speed = 5):
        GameObject.update(self, speed)
        
        if self.enemy == False:
            self.rect.y -= speed
            if self.rect.y < 0:
                self.kill()
        else:
            self.rect.y += speed
            if self.rect.y > self.game.HEIGHT:
                self.kill()