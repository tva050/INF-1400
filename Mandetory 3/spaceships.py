import pygame 
from pygame import Vector2 as Vec2
import math
import numpy as np
from config import Config

class Spaceships(pygame.sprite.Sprite):
    def __init__(self, image, start_position):
        super().__init__() #
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (90/1.5, 64/1.5))
        self.rect = self.image.get_rect()
        self.rect.x = start_position[0]
        self.rect.y = start_position[1]
        self.rect.center = [self.rect.x, self.rect.y]
        self.angle = Config.START_ANGLE
        
    def draw(self): 

        return Config.SCREEN.blit(self.image, self.rect)
    
    def update(self):
        self.rect = self.draw()
    
    
        
        
    
        

    

        
    
        
        