import pygame
from config import Config

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.load(Config.PLATFORM).convert_alpha()
        self.image = pygame.transform.scale(self.image, (71.9, 54))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.screen = Config.SCREEN
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
    