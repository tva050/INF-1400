""" 
Writen by: Trym Varland
"""
import pygame
from config import *
from pygame import Vector2 as Vec2
import numpy as np

""" _______SPACESHIPS_______ """
class Spaceships(pygame.sprite.Sprite):
    """ 
    A class to represent the spaceship in the game.
    
    ...

    Attributes
    ----------
    image : pygame.Surface
        The image of the spaceship
    rect : pygame.Rect
        The rectangle of the spaceship
    screen : pygame.Surface
        The screen the spaceship is drawn on
    
    Methods
    -------
    move()
        Moves the spaceship in the direction of the spaceship
    thrust()
        Gives the spaceship thrust
    move_right()
        Rotates the spaceship to the right
    move_left()
        Rotates the spaceship to the left
    boundaries()
        Checks if the spaceship is within the boundaries of the screen
    draw()
        Draws the spaceship on the screen
    update()
        Updates the spaceship
    reset() 
        Resets the spaceship to its original position
    """
    def __init__(self, image, position, velocity):
        """ 
        Constructs all the necessary attributes for the spaceship object.
    
        Parameters
        ----------  
            image : str
                The image of the spaceship
            position : tuple
                The position of the spaceship
            speed : int
                The speed of the spaceship
        """
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, SPACESHIP_SIZE).convert_alpha() # Scale the image
        self.image_width, self.image_height = self.image.get_size() # Get the size of the image
        self.mask = pygame.mask.from_surface(self.image) # Mask for collision detection
        
        self.start_pos = position # The starting position of the spaceship
        self.velocity = Vec2(velocity) # The velocity of the spaceship
        self.position = Vec2(position) # The position of the spaceship
        self.angle = np.degrees(0) # The angle of the spaceship
        
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y)) # The rectangle of the spaceship
        
        self.shoot_cooldown = 0 # The cooldown of the spaceship
        self.beams = pygame.sprite.Group() # The group of the laser beams
        
        self.fuel = MAX_FUEL # The fuel of the spaceship
        self.score = SCORE # The score of the spaceship
        
        self.screen = SCREEN # The screen the spaceship is drawn on
        
    # Writen with help from Håkon Silseth    
    def move(self):
        """ 
        Moves the spaceship in the direction of the spaceship

        Parameters
        ----------
        None
        """
        self.position += self.velocity # Add the velocity to the position
        self.velocity += Vec2(0, GRAVITY) # Add gravity to the velocity
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y)) # Update the rectangle of the spaceship
        
    def thrust(self):
        """ 
        Gives the spaceship thrust
    
        Parameters
        ----------
        None
        """
        if self.fuel > 0: # If the spaceship has fuel
            thrust_vector = Vec2(0, THRUST) # The thrust vector
            thrust_vector.rotate_ip(-self.angle+180) # Rotate the thrust vector
            self.velocity += thrust_vector # Add the thrust vector to the velocity
            self.fuel -= FUEL_CONSUMPTION # Reduce the fuel of the spaceship
        
    def move_right(self, image):
        """ 
        Rotates the spaceship to the right
        
        Parameters
        ----------
        image : str
            The image of the spaceship
        """
        self.angle -= np.degrees(ROTATION_SPEED) # Rotate the spaceship
        rotate_image = pygame.transform.rotate(image, self.angle) # Rotate the image
        rotate_rec = rotate_image.get_rect(center = self.rect.center) # Rotate the rectangle
        return rotate_image, rotate_rec
    
    def move_left(self, image):
        """ 
        Rotates the spaceship to the left
        
        Parameters
        ----------
        image : str
            The image of the spaceship
        """
        self.angle += np.degrees(ROTATION_SPEED)
        rotate_image = pygame.transform.rotate(image, self.angle)
        rotate_rec = rotate_image.get_rect(center = self.rect.center)
        return rotate_image, rotate_rec
    
    def boundaries(self):
        """ 
        Checks if the spaceship is within the boundaries of the screen
    
        Parameters
        ----------
        None
        """
        if self.position.x < 0:
            self.velocity.x = -self.velocity.x
        elif self.position.x > SCREEN_WIDTH:
            self.velocity.x = -self.velocity.x
        if self.position.y < 0:
            self.velocity.y = -self.velocity.y
        elif self.position.y > SCREEN_HEIGHT:
            self.velocity.y = -self.velocity.y
        
    
    def draw(self):
        """ 
        Draws the spaceship on the screen
        
        Parameters
        ----------
        None
        """
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """
        
        Updates the spaceship
        
        Parameters
        ----------
        None
        """
        
        self.move()
        self.draw()
        self.boundaries()
        
        if self.shoot_cooldown > 0: # If the spaceship is on cooldown
            self.shoot_cooldown -= 1 # Reduce the cooldown

    def reset(self):
        """ 
        Resets the spaceship to its original position
    
        Parameters
        ----------
        None
        """
        self.position = Vec2(self.start_pos)
        self.velocity = Vec2(0, 0)
        self.angle = np.degrees(0)
        self.fuel = MAX_FUEL
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
        self.rect.center = self.position