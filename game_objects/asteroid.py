from game_object import GameObject

'''
Created on Apr 6, 2015

@author: ytsonev
'''

class Asteroid(GameObject):
    WIDTH = 87
    HEIGHT = 87
    IMAGE = 'asteroid.png'
    
    def __init__(self, position):
        super(Asteroid, self).__init__(position)