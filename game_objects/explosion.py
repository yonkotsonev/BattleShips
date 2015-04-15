from game_object import GameObject

'''
Created on Apr 6, 2015

@author: ytsonev
'''

class Explosion(GameObject):
    WIDTH = 128;
    HEIGHT = 128;
    IMAGE = 'boom.gif'
    
    def __init__(self, position):
        super(Explosion, self).__init__(position)