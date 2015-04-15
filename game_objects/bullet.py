from game_object import GameObject

'''
Created on Apr 6, 2015

@author: ytsonev
'''

class Bullet(GameObject):
    WIDTH = 13
    HEIGHT = 35
    IMAGE = 'bullet.png'
    
    def __init__(self, position):
        super(Bullet, self).__init__(position)