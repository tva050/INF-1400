""" 
Writen by: Trym Varland

module:: obstacles.py 
    This module contains the Obstacles class.
"""
import pygame
from config import *

class Obstacles(pygame.sprite.Sprite):
    """ 
    This class is used to create obstacles for the game.
    
    ...

    Attributes
    ----------
    image : pygame.Surface
        The image of the obstacle
    rect : pygame.Rect
        The rectangle of the obstacle
    screen : pygame.Surface
        The screen the obstacle is drawn on
    
    Methods
    -------
    draw()
        Draws the obstacle on the screen
    update()
        Updates the obstacle
    """
    def __init__(self, image, position):
        """ 
        Constructs all the necessary attributes for the obstacle object.
        
        Parameters
        ----------
            image : str
                The image of the obstacle
            position : tuple
                The position of the obstacle
        """
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, OBSTACLE_SIZE).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image) # Mask of the image, used for collision detection
        
        self.rect = self.image.get_rect()
        self.rect.center = [position[0], position[1]]
        
        self.screen = SCREEN
    
    def draw(self):
        """ 
        Draws the obstacle on the screen.

        Parameters
        ----------
            None
        """
        self.screen.blit(self.image, self.rect)
    def update(self):
        """ 
        Updates the obstacle.
    
        Parameters
        ----------
            None
        """
        self.draw()
    
    
        
    
    
        
    

        