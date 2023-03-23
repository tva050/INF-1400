import pygame
from config import Config

class Obstacles(pygame.sprite.Sprite):
    def __init__(self ,x_position, y_position): 
        super().__init__()
        self.image = pygame.image.load(Config.OBSTACLE).convert_alpha()
        self.image = pygame.transform.scale(self.image, Config.OBSTACLE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = [x_position, y_position]       
        
    def draw(self):
        Config.SCREEN.blit(self.image, self.rect)
    
    
    
        
    
    
        
    

        