""" 
Wirten by: Trym Varland
"""

import pygame
from config import Config

""" _______PLATFORMS_______ """

class Platforms(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(Config.PLATFORM_IMG)
        self.image = pygame.transform.scale(self.image, Config.PLATFORM_SIZE).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.screen = Config.SCREEN
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        self.draw()
        