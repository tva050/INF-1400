import pygame
from config import Config
import random

class Obstacles:
    def __init__(self, image, screen):
        self.image = pygame.image.load(image).convert_alpha()
        self.screen = screen
        self.rect = self.image.get_rect()
    
    def draw(self):
        self.rect.x = random.randint(0, Config.SCREEN_WIDTH)
        self.rect.y = random.randint(0, Config.SCREEN_HEIGHT)
        self.screen.blit(self.image, self.rect)
    
    

        