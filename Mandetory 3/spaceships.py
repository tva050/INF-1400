""" 
Wirten by: Trym Varland
"""
import pygame
from config import Config
from pygame import Vector2 as Vec2
import numpy as np

""" _______SPACESHIPS_______ """
class Spaceships(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, Config.SPACESHIP_SIZE).convert_alpha()
        self.image_width, self.image_height = self.image.get_size()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.start_pos = position
        self.velocity = Vec2(speed)
        self.position = Vec2(position)
        self.angle = np.degrees(0)
        
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
        
        self.shoot_cooldown = 0
        self.beams = pygame.sprite.Group()
        
        self.fuel = Config.MAX_FUEL
        self.score = Config.SCORE
        
        self.screen = Config.SCREEN
        
    # Writen with help from Håkon Silseth    
    def move(self):
        self.position += self.velocity
        self.velocity += Vec2(0, Config.GRAVITY)
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
        
    def thrust(self):
        if self.fuel > 0:
            thrust_vector = Vec2(0, Config.THRUST)
            thrust_vector.rotate_ip(-self.angle+180)
            self.velocity += thrust_vector
            self.fuel -= Config.FUEL_CONSUMPTION
        
    def move_right(self, image):
        self.angle -= np.degrees(Config.ROTATION_SPEED)
        rotate_image = pygame.transform.rotate(image, self.angle)
        rotate_rec = rotate_image.get_rect(center = self.rect.center)
        return rotate_image, rotate_rec
    
    def move_left(self, image):
        self.angle += np.degrees(Config.ROTATION_SPEED)
        rotate_image = pygame.transform.rotate(image, self.angle)
        rotate_rec = rotate_image.get_rect(center = self.rect.center)
        return rotate_image, rotate_rec
    
    def boundaries(self):
        if self.position.x < 0:
            self.velocity.x = -self.velocity.x
        elif self.position.x > Config.SCREEN_WIDTH:
            self.velocity.x = -self.velocity.x
        if self.position.y < 0:
            self.velocity.y = -self.velocity.y
        elif self.position.y > Config.SCREEN_HEIGHT:
            self.velocity.y = -self.velocity.y
        
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        self.move()
        self.draw()
        self.boundaries()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def reset(self):
        self.position = Vec2(self.start_pos)
        self.velocity = Vec2(0, 0)
        self.angle = np.degrees(0)
        self.fuel = Config.MAX_FUEL
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
        self.rect.center = self.position