""" 
Wirten by: Trym Varland
"""

import pygame
from pygame import Vector2 as Vec2
from config import Config

""" _______LASER_BEAM_______ """

class LaserBeam(pygame.sprite.Sprite):
    def __init__(self, image, position, angle):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (41, 11)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = Config.BEAM_VELOCITY
    
        self.position = Vec2(position)
        self.speed = Vec2(0, 0)
        self.angle = angle
        
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
        
        self.screen = Config.SCREEN
        
    def draw(self):
        self.screen.blit(self.image, self.rect) 
    
    # Move the beam in the direction of the spaceship 
    def move(self):
        self.position += Vec2(self.velocity, 0).rotate(-self.angle-90)
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
        
    def update(self):
        self.move()
        self.draw()