import sys
import pygame
from game_objects import Ship, Bullet, Asteroid, Star
from levels.level1 import Level1
from event_manager import EventManager
from game_objects.explosion import Explosion

class Game(object):    
    TITLE = 'BATTLE SHIPS'

    WIDTH = 800
    HEIGHT = 600
    
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (127,0,0)
    
    def __init__(self):
        pygame.init()
        
        pygame.mixer.init()
        self.fireSound = 'sounds/fire.wav'
        self.explosionSound = 'sounds/explosion.wav'
        
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.TITLE)
        self.clock = pygame.time.Clock()
        
        self.eventManager = EventManager(self)
        
        self.player = None
        self.sprites = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        
        for x in range(30):
            self.CreateStar()
            
        self.gameCompleted = False
        
        self.levels = [
           Level1(self),
        ]
        
    def SetBackGround(self, image = None, color = BLACK):
        self.screen.fill(color)
        
        if image is not None:
            self.screen.blit(image, image.get_rect())
        
    def WriteText(self, text, surFace, position, fontSize = 36, color = WHITE):
        font = pygame.font.Font(None, fontSize)
        text = font.render(text, 1, color)

        surFace.blit(text, position)
        
    def Run(self):
        self.score = 0
        self.player = Ship(self)
        self.player.rect.x = self.WIDTH/2 - self.player.rect.width/2
        self.player.rect.y = self.HEIGHT - self.player.rect.height
        self.sprites.add(self.player)
        
        self.PlayBackGroundMusic('sounds/theme.mp3')
        
        for level in self.levels:
            self.RunLevel(level)

        if self.player.alive():
            self.Win()
            
    def RunLevel(self, level):
        self.LevelStart(level)
            
        while level.levelComplete == False:
            self.eventManager.PreProcess()
            for event in pygame.event.get():
                self.eventManager.ProcessEvent(event)
                
            self.SetBackGround(level.background)
                            
            self.Update()
            level.GameLogic()
            self.CheckForCollisions()
            self.Draw()
            self.RefreshScreen()
            
        self.LevelEnd(level)
            
    def LevelStart(self, level):
        self.ClearObjects()
        
        start = False
        while start == False:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    self.Quit();
                if event.type == pygame.locals.KEYDOWN:
                    start = True

            self.SetBackGround(level.background)
            self.sprites.update()
            self.sprites.draw(self.screen)
            self.WriteText(str(level), self.screen, (330,250), 50, Game.WHITE)
            self.WriteText('(Press Any Key To Start)', self.screen, (295,300), 25, Game.RED)
            self.RefreshScreen()
                
    def LevelEnd(self, level):
        self.ClearObjects()
        
        self.player.rect.x = self.WIDTH/2 - self.player.rect.width/2
        self.player.rect.y = self.HEIGHT - self.player.rect.height
        
        self.GetLevelBonus(level)
        
        for x in range(1,800 - self.player.rect.height):
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    self.Quit();

            self.player.rect.y -= 1
            self.SetBackGround(level.background)
            
            self.sprites.update()
            self.sprites.draw(self.screen)
            
            self.WriteText(str(level) + ' COMPLETE', self.screen, (230,200), 50, Game.WHITE)
            
            self.RefreshScreen()
            
    def GetLevelBonus(self, level): 
        bonus = level.bonus
        
        while bonus > 0:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    self.Quit();
            
            if self.player.health < 100:
                self.player.health += 1
                bonus -= 5
                
                self.clock.tick(20)
            else:
                self.score += 1
                bonus -= 1
                
            self.PlaySound('sounds/bonus.wav')
            
            self.SetBackGround(level.background)
            self.sprites.update()
            self.sprites.draw(self.screen)
            
            self.WriteText(str(level) + ' COMPLETE', self.screen, (230,200), 50, Game.WHITE)
            
            self.WriteText('BONUS = ' + str(bonus), self.screen, (230,250), 50, Game.WHITE)
            
            self.WriteText('SCORE = ' + str(self.score), self.screen, (230,300), 50, Game.WHITE)
        
            health = '|' * (self.player.health / 5)
            self.WriteText('HEALTH', self.screen, (230,350), 50, Game.WHITE)
            self.WriteText(health, self.screen, (380,350), 50, Game.RED)
            
            self.RefreshScreen()
            
    def ClearObjects(self):
        self.sprites.empty()
        self.asteroids.empty()
        self.bullets.empty()
        self.enemies.empty()
        
        self.sprites.add(self.stars)
        self.sprites.add(self.player)

    def RefreshScreen(self):
        pygame.display.flip()
        self.clock.tick(50)
        
    def Update(self):
        self.sprites.update()
        
    def Draw(self):
        self.sprites.draw(self.screen)
        
        if self.player.alive() == False:
            self.WriteText('Game Over', self.screen, (320,250), 50, Game.RED)
            self.WriteText('(Press Esc To Quit Or F2 To Restart)', self.screen, (260,300), 25, Game.WHITE)
            
        self.WriteText('Score = ' + str(self.score), self.screen, (10,10), 30, Game.WHITE)
        
        health = '|' * (self.player.health / 5)
        self.WriteText('HEALTH', self.screen, (550,10), 30, Game.WHITE)
        self.WriteText(health, self.screen, (650,10), 30, Game.RED)
        
        if self.gameCompleted == True:
            self.WriteText('You Won! Congratulations!', self.screen, (180,250), 50, Game.RED)
            self.WriteText('(Press Esc To Quit Or F2 To Restart)', self.screen, (250,300), 25, Game.WHITE)
        
    def Quit(self):
        pygame.quit()
        sys.exit()
        
    def Fire(self, obj = None):
        if obj is None:
            obj = self.player
            
        if obj.alive() == False:
            return
        
        rect = obj.rect
        bullet = Bullet(self)
        bullet.rect.x = rect.x + rect.width/2 - bullet.rect.width/2
        bullet.rect.y = rect.y -  bullet.rect.height 
        
        self.bullets.add(bullet)
        self.sprites.add(bullet)
        
    def Restart(self):
        self.__init__()
        self.Run()
        
    def GoLeft(self, obj = None):
        if obj is None:
            obj = self.player
            
        if obj.alive() == False:
            return
        
        self.player.GoLeft()
        
    def GoRight(self, obj = None):
        if obj is None:
            obj = self.player
            
        if obj.alive() == False:
            return
        
        self.player.GoRight()
        
    def CreateAsteroid(self):
        asteroid = Asteroid(self)
        self.asteroids.add(asteroid)
        self.sprites.add(asteroid)
        
    def CreateStar(self):
        star = Star(self)
        self.stars.add(star)
        self.sprites.add(star)
        
    def CheckForCollisions(self):
        hitedObjects = []
        for obj in self.bullets:
            hits = pygame.sprite.spritecollide(obj, self.asteroids, True)
            if len(hits) > 0:
                obj.kill()
            hitedObjects += hits
            
        for obj in hitedObjects:
            self.score += 5
            
            explosion = Explosion(self)
            explosion.rect.x = obj.rect.x
            explosion.rect.y = obj.rect.y
            self.explosions.add(explosion)
            self.sprites.add(explosion)
            
        hitedObjects = []
        for obj in self.bullets:
            hits = pygame.sprite.spritecollide(obj, self.enemies, True)
            if len(hits) > 0:
                obj.kill()
            hitedObjects += hits
            
        for obj in hitedObjects:
            self.score += 10
            
            explosion = Explosion(self)
            explosion.rect.x = obj.rect.x
            explosion.rect.y = obj.rect.y
            self.explosions.add(explosion)
            self.sprites.add(explosion)
            
        hitedObjects = []
        for obj in self.asteroids:
            hits = pygame.sprite.spritecollide(obj, self.enemies, True)
            if len(hits) > 0:
                obj.kill()
                
                explosion = Explosion(self)
                explosion.rect.x = obj.rect.x
                explosion.rect.y = obj.rect.y
                self.explosions.add(explosion)
                self.sprites.add(explosion)
            hitedObjects += hits
            
        for obj in hitedObjects:
            self.score += 1
            
            explosion = Explosion(self)
            explosion.rect.x = obj.rect.x
            explosion.rect.y = obj.rect.y
            self.explosions.add(explosion)
            self.sprites.add(explosion)
            
        if self.player.alive():
            asteroidhits = pygame.sprite.spritecollide(self.player, self.asteroids, True)
            for obj in asteroidhits:
                self.player.Hit(5)
                
                explosion = Explosion(self)
                explosion.rect.x = obj.rect.x
                explosion.rect.y = obj.rect.y
                self.explosions.add(explosion)
                self.sprites.add(explosion)
                
            bullethits = pygame.sprite.spritecollide(self.player, self.bullets, True)
            for obj in bullethits:
                self.player.Hit(2)
                
                explosion = Explosion(self)
                explosion.rect.x = obj.rect.x
                explosion.rect.y = obj.rect.y
                self.explosions.add(explosion)
                self.sprites.add(explosion)
                
            enemyhits = pygame.sprite.spritecollide(self.player, self.enemies, True)
            for obj in enemyhits:
                explosion = Explosion(self)
                explosion.rect.x = obj.rect.x
                explosion.rect.y = obj.rect.y
                self.explosions.add(explosion)
                self.sprites.add(explosion)
                
                self.player.Hit(10)
                
            if self.player.health <= 0:
                self.player.kill()
                    
    def Win(self):
        self.gameCompleted = True
        eventManager = EventManager(self)
        while True:
            for event in pygame.event.get():
                eventManager.ProcessEvent(event)
                
            self.SetBackGround()
            self.sprites.update()
            self.Draw()
            self.RefreshScreen()
            
    def PlayBackGroundMusic(self, musicFile):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(musicFile)
        pygame.mixer.music.play(-1)
            
    def PlaySound(self, sound):
        pygame.mixer.Sound(sound).play()