from game_object import GameObject

'''
Created on Apr 6, 2015

@author: ytsonev
'''

class Ship(GameObject):
    WIDTH = 103
    HEIGHT = 100
    IMAGE = 'ship.png'
    
    def __init__(self, position):
        super(Ship, self).__init__(position)