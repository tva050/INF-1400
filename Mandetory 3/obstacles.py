import pygame
from config import Config

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, Config.OBSTACLE_SIZE).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()
        self.rect.center = [position[0], position[1]]
        
        self.screen = Config.SCREEN
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.draw()
    
    
        
    
    
        
    

        