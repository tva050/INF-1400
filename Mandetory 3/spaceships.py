import pygame 
from pygame import Vector2 as Vec2
from config import Config

class Spaceships(pygame.sprite.Sprite):
    def __init__(self, image, screen ,start_pos):
        super().__init__() #
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (71.9, 54))
        self.screen = screen
        self.start_pos = start_pos
        self.rect = self.image.get_rect()
        self.rect.x = self.start_pos[0]
        self.rect.y = self.start_pos[1]
        
    def draw(self): 
        
        
        self.screen.blit(self.image, self.start_pos)
        
    
        

    

        
    
        
        