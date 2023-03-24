import pygame
from config import Config

""" _______LASER_BEAM_______ """

class LaserBeam(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (20, 20)).convert_alpha()

        #self.max_beams = Config.MAX_BEAMS
        self.velocity = Config.BEAM_VELOCITY
    
         
        self.x, self.y = position

        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.rect.center = (self.x, self.y)

        self.screen = Config.SCREEN
    
    def draw(self):
        self.screen.blit(self.image, self.rect) 
    
    def move(self):
        self.rect.y -= self.velocity 
        if self.rect.y < 0 or self.rect.y > Config.SCREEN_HEIGHT:
            self.kill()
        if self.rect.x < 0 or self.rect.x > Config.SCREEN_WIDTH:
            self.kill()
    def update(self):
        self.move()
        self.draw()