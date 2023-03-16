import pygame
from config import Config

class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, position):
        super().__init__()
        self.image = pygame.image.load(Config.PLATFORM).convert()
        self.image = pygame.transform.scale(self.image, (71.9, 54))
        self.screen = screen
        self.position = position
        self.rect = self.image.get_rect()
        
    def draw(self):
        self.screen.blit(self.image, self.position)
    
    def update(self):
        self.draw()