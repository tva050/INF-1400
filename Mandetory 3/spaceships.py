import pygame 
from pygame import Vector2 as Vec2
import math
import numpy as np
from config import Config

class Spaceships(pygame.sprite.Sprite):
    def __init__(self, image, start_position, id):
        super().__init__() #
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (90/1.5, 64/1.5))
        self.rect = self.image.get_rect()
        self.rect.x = start_position[0]
        self.rect.y = start_position[1]
        self.rect.center = [self.rect.x, self.rect.y]
        self.angle = Config.START_ANGLE
        self.gravity = Config.GRAVITY 
        #self.speed.x = speed[0]
        #self.speed.y = speed[1]
    
        
    def draw(self):
        Config.SCREEN.blit(self.image, self.rect)
   
   
    def spaceship_player1_move(self):
        if id == 1:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w]:
                self.player1_spaceship.move_up()
            if pressed[pygame.K_s]:
                self.player1_spaceship.move_down()
            if pressed[pygame.K_a]:
                self.player1_spaceship.move_left()
            if pressed[pygame.K_d]:
                self.player1_spaceship.move_right()
        
        if id == 2:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                self.player2_spaceship.move_up()
            if pressed[pygame.K_DOWN]:
                self.player2_spaceship.move_down()
            if pressed[pygame.K_LEFT]:
                self.player2_spaceship.move_left()
            if pressed[pygame.K_RIGHT]:
                self.player2_spaceship.move_right()

    
    def update(self):
        self.movement()
        self.draw()
    
    
        
        
    
        

    

        
    
        
        