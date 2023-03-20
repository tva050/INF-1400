import pygame 
from pygame import Vector2 as Vec2
import math
import numpy as np
from config import Config

class Spaceships(pygame.sprite.Sprite):
    def __init__(self, image, start_position, speed):
        super().__init__() #
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (90/1.5, 64/1.5))
        self.rect = self.image.get_rect()
        self.rect.x = start_position[0]
        self.rect.y = start_position[1]
        self.rect.center = [self.rect.x, self.rect.y]
        self.angle = Config.START_ANGLE
        self.gravity = Config.GRAVITY 
        self.speed.x = speed[0]
        self.speed.y = speed[1]
    
        
    def draw(self):
        Config.SCREEN.blit(self.image, self.rect)
    
    def movement(self):
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y
        self.speed.y += self.gravity
        self.speed.x += self.gravity
        self.rect.center = [self.rect.x, self.rect.y]


    
    def update(self):
        self.movement()
        self.draw()
    
    
        
        
    
        

    

        
    
        
        