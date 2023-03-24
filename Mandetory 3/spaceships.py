import pygame
from pygame import Vector2 as Vec2
import math
from config import Config


class Spaceships(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, Config.SPACESHIP_SIZE).convert_alpha()
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        
        self.start_pos = position
        
        self.velocity = Vec2(0, 0)
        self.acceleration = 0 
        
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        
    
        self.clock = pygame.time.Clock()
        self.time = self.clock.tick(30)/1000 # Time in seconds
        
        self.screen = Config.SCREEN
        self.gravity = Config.GRAVITY
        
        #self.fired_beam_state = False
        self.shoot_cooldown = 0
        
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    
    def spaceship_boundaries(self):
        if self.rect.x  > Config.SCREEN_WIDTH:
            self.velocity.x = -1
        elif self.rect.x < 0:
            self.velocity.x = 1
        elif self.rect.y > Config.SCREEN_HEIGHT - self.image_height:
            self.velocity.y = -1
        elif self.rect.y < 0:   
            self.velocity.y = 1
        
    def move(self, dx, dy):
        self.rect.x += dx + self.acceleration * self.time
        self.rect.y += dy + self.acceleration * self.time
        
    def thrust(self, velocity):
        self.velocity.y = -velocity
    def move_right(self, velocity):
        self.velocity.x = velocity 
    def move_left(self, velocity):
        self.velocity.x = -velocity
    
    def update(self):
        self.move(self.velocity.x, self.velocity.y)
        self.spaceship_boundaries() 
        
        self.velocity.y += min(1, self.gravity)
        self.velocity.x = 0
        
        self.draw()
        
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def reset(self):
        self.rect.x = self.start_pos[0]
        self.rect.y = self.start_pos[1]
        self.velocity = Vec2(0, 0)
        self.acceleration = 0
        self.rect.centerx = self.start_pos[0]
        self.rect.centery = self.start_pos[1]
        

        
        
    
        

    

        
    
        
        