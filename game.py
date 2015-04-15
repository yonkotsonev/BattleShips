import sys
import pygame
from position import Position
from game_objects import Ship, Bullet, Asteroid, Explosion
from levels.level1 import Level1
from event_manager import EventManager


class Game(object):    
    TITLE = 'BATTLE SHIPS'

    WIDTH = 800
    HEIGHT = 600
    
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (127,0,0)
    
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.TITLE)
        self.__clock = pygame.time.Clock()
        
        self.__player = None
        self.__asteroids = []
        self.__bullets = []
        self.__explosions = []
        self.__gameCompleted = False
        
    def SetBackGround(self, color = BLACK):
        self.__screen.fill(color)
        
    def WriteText(self, text, surFace, position, fontSize = 36, color = WHITE):
        font = pygame.font.Font(None, fontSize)
        text = font.render(text, 1, color)

        surFace.blit(text, position)
        
    def Run(self):
        self.__score = 0
        self.__player = Ship(Position(self.WIDTH /2 - Ship.WIDTH/2, self.HEIGHT - Ship.HEIGHT))
            
        level = Level1(self)
        level.run()
        
        if self.__player.IsAlive():
            self.Win()
    
    def DrawImage(self, imageFile, position = None):
        image = pygame.image.load('images/' + str(imageFile)).convert_alpha()
        
        if position is None:
            position = image.get_rect()
        elif isinstance(position, Position):
            position = position.ToTuple()
        
        self.__screen.blit(image, position)
        
    def GetEvents(self):
        for event in pygame.event.get():
            yield event
            
    def RefreshScreen(self):
        pygame.display.flip()
        self.__clock.tick(50)
        
    def Draw(self):
        for arr in self.__explosions:
            arr[0].Draw(self)
            
            if arr[1] == 0:
                self.__explosions.remove(arr)
            else:
                arr[1] -= 1
            
        for obj in self.__asteroids:
            obj.Draw(self)
            
        for obj in self.__bullets:
            obj.Draw(self)
            
        if self.__player.IsAlive():
            self.__player.Draw(self)
        else:
            self.WriteText('Game Over', self.__screen, (320,250), 50, Game.RED)
            self.WriteText('(Press Esc To Quit Or F2 To Restart)', self.__screen, (250,300), 25, Game.WHITE)
            
        self.WriteText('Score = ' + str(self.__score), self.__screen, (10,10), 30, Game.WHITE)
        
        if self.__gameCompleted == True:
            self.WriteText('You Won! Congratulations!', self.__screen, (180,250), 50, Game.RED)
            self.WriteText('(Press Esc To Quit Or F2 To Restart)', self.__screen, (250,300), 25, Game.WHITE)
        
    def Quit(self):
        pygame.quit()
        sys.exit()
        
    def Fire(self, obj = None):
        if obj is None:
            obj = self.__player
            
        if obj.IsAlive() == False:
            return
        
        y = obj.Position().Y() - Bullet.HEIGHT;
        x = obj.Position().X() + (obj.WIDTH/2 - Bullet.WIDTH/2)
        
        self.__bullets.append(Bullet(Position(x,y)))
        
    def Restart(self):
        self.__init__()
        self.Run()
        
    def GoLeft(self, obj = None):
        if obj is None:
            obj = self.__player
            
        if obj.IsAlive() == False:
            return
        
        self.__player.GoLeft()
        
    def GoRight(self, obj = None):
        if obj is None:
            obj = self.__player
            
        if obj.IsAlive() == False:
            return
        
        self.__player.GoRight()
        
    def CreateAsteroid(self, position):
        self.__asteroids.append(Asteroid(position))
        
    def CheckForCollisions(self):
        for obj in self.__asteroids:
            if obj.CheckForCollision(self.__player) and self.__player.IsAlive():
                obj.Kill()
                self.__player.Kill()
                self.__explosions.append([Explosion(self.__player.Position()), 10])
                continue
                
            for bullet in self.__bullets:
                if obj.CheckForCollision(bullet):
                    obj.Kill()
                    bullet.Kill()   
                    self.__explosions.append([Explosion(obj.Position()), 10])
                    self.__score += 5
                    continue
                
    def GetAstroids(self):
        return self.__asteroids
        
    def GetBullets(self):
        return self.__bullets
        
    def ClearDeadObjects(self):
        objects = self.__asteroids + self.__bullets
        for obj in objects:
            if obj.IsAlive() == False:
                if obj in self.__asteroids:
                    self.__asteroids.remove(obj)
                elif obj in self.__bullets:    
                    self.__bullets.remove(obj)
                    
    def Win(self):
        self.__gameCompleted = True
        eventManager = EventManager(self)
        while True:
            for event in self.GetEvents():
                eventManager.ProcessEvent(event)
                
            self.Draw()
            self.RefreshScreen()