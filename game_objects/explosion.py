from game_object import GameObject

class Explosion(GameObject):
    def __init__(self, game, time = 5):
        super(Explosion, self).__init__('boom.gif', game)
        
        self.time = time
       
    def update(self, *args):
        GameObject.update(self, *args)
        self.game.PlaySound(self.game.explosionSound)
        self.time -= 1
        if self.time <= 0:
            self.kill()