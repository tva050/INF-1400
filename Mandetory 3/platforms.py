""" 
Writen by: Trym Varland

module:: platforms.py
    This module contains the Platforms class. This class is used to create the platforms for the game.
"""

import pygame
from config import *

""" _______PLATFORMS_______ """

class Platforms(pygame.sprite.Sprite):
    """ 
    A class to represent the platforms in the game.
    
    ...
    
    Attributes
    ----------
    image : pygame.Surface
        The image of the platform
    rect : pygame.Rect
        The rectangle of the platform
    screen : pygame.Surface
        The screen the platform is drawn on
        
    Methods
    ------- 
    draw()
        Draws the platform on the screen
    update()
        Updates the platform
    """
    def __init__(self, pos_x, pos_y):
        """ 
        Constructs all the necessary attributes for the platform object.
        
        Parameters
        ----------
            pos_x : int
                The x position of the platform
            pos_y : int
                The y position of the platform
        """
        super().__init__()
        self.image = pygame.image.load(PLATFORM_IMG)
        self.image = pygame.transform.scale(self.image, PLATFORM_SIZE).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.screen = SCREEN
        
    def draw(self):
        """ 
        Draws the platform on the screen.
        
        Parameters
        ----------
            None

        Returns
        -------
            Blits the platform on the screen
        """
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """ 
        Updates the platform.    
        """
        self.draw()
        