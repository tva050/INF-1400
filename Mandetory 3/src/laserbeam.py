""" 
Writen by: Trym Varland

module:: laserbeam.py
    This module contains the LaserBeam class. This class is used to create the laser beam for the game.
"""

import pygame
from pygame import Vector2 as Vec2
from config import *

""" _______LASER_BEAM_______ """

class LaserBeam(pygame.sprite.Sprite):
    """ 
    A class to represent the laser beam in the game.
    
    ...

    Attributes
    ----------
    image : pygame.Surface
        The image of the laser beam
    rect : pygame.Rect
        The rectangle of the laser beam
    screen : pygame.Surface
        The screen the laser beam is drawn on

    Methods
    -------
    draw()
        Draws the laser beam on the screen
    move()
        Moves the laser beam in the direction of the spaceship
    update()
        Updates the laser beam
    """
    def __init__(self, image, position, angle):
        """ 
        Constructs all the necessary attributes for the laser beam object.
        
        Parameters
        ----------
            image : str
                The image of the laser beam
            position : tuple
                The position of the laser beam
            angle : int
                The angle of the laser beam
        """
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (41, 11)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = BEAM_VELOCITY 
    
        self.position = Vec2(position) # Position of the laser beam
        self.speed = Vec2(0, 0) # Speed of the laser beam
        self.angle = angle # Angle of the laser beam
        
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
        
        self.screen = SCREEN
        
    def draw(self):
        """ 
        Draws the laser beam on the screen.
    
        Parameters
        ----------
            None
        """
        self.screen.blit(self.image, self.rect) 
    
    # Move the beam in the direction of the spaceship 
    def move(self):
        """ 
        Moves the laser beam in the direction of the spaceship.
    
        Parameters
        ----------
            None
        """
        self.position += Vec2(self.velocity, 0).rotate(-self.angle-90) # Rotate the vector
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y)) # Update the rect
        
    def update(self):
        """ 
        Updates the laser beam.
    
        Parameters
        ----------
            None
        """
        self.move()
        self.draw()