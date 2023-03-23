import pygame
from pygame import Vector2 as Vec2
import math
from config import Config


""" _______SPACESHIPS_______ """
class Spaceships(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, Config.SPACESHIP_SIZE).convert_alpha()
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        
        """ 
        self.x_velocity = 0
        self.y_velocity = 0
        self.velocity = 0
        
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        """
        
        self.x_velocity, self.y_velocity = Vec2(0, 0)
        self.position = Vec2(position)
        self.angle = self.x_velocity, self.y_velocity
        
        self.screen = Config.SCREEN
        self.gravity = Config.GRAVITY
        
    def draw(self):
        self.screen.blit(self.image, self.position)
    
    def spaceship_boundaries(self):
        if self.position.x  > Config.SCREEN_WIDTH:
            self.x_velocity = -1
        elif self.position.x < 0:
            self.x_velocity = 1
        elif self.position.y > Config.SCREEN_HEIGHT - self.image_height:
            self.y_velocity = -1
        elif self.position.y < 0:   
            self.y_velocity = 1
    
    """ def move(self, dx, dy):
        self.position.x += dx 
        self.position.y += dy """
        
    def move(self, dx, dy):
        self.position.x += dx
        self.position.y += dy
    
    
    def thrust(self, velocity):
        self.y_velocity = -velocity
    def move_right(self, velocity):
        self.x_velocity = velocity 
    def move_left(self, velocity):
        self.x_velocity = -velocity  
    
    def update(self):
        self.move(self.x_velocity, self.y_velocity)
        self.spaceship_boundaries()
        
        self.y_velocity += min(1, self.gravity)
        self.x_velocity = 0
    
        self.draw()
        
        

        
        
    
        

    

        
    
        
        