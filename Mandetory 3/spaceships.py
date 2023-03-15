import pygame 
from config import Config

class Spaceships(pygame.sprite.Sprite):
    def __init__(self, image, screen ,start_pos):
        self.image = pygame.image.load(image).convert_alpha()
        self.screen = screen
        self.start_pos = start_pos
        x_pos, y_pos = start_pos
        
    def draw(self):
        self.screen.blit(self.image, (x_pos, y_pos))
        
        
        