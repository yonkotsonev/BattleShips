import pygame

class GameObject(pygame.sprite.Sprite):
    
    def __init__(self, image, game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/' + image).convert_alpha()
        self.rect = self.image.get_rect()
        self.game = game
        
    def update(self, *args):
        pygame.sprite.Sprite.update(self, *args)