import pygame 
import numpy as np

class Config():
    """ 
    Contains:
     - Screen size
     - Screen title
     - Amount of gravity 
     - Amount of starting fuel
    """
    pygame.init()
    pygame.display.set_caption("Shadow of the Moon")
    
    # Screen specifications
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    # Screen
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
    
    # Background image
    BACKGROUND = pygame.image.load("assets\space_background.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() 
    
    # Player images
    PLAYER1_IMG = "assets\spaceship1.png" 
    PLAYER2_IMG = "assets\spaceship2.png"
    START_POSITION_PLAYER1 = (SCREEN_WIDTH-840, SCREEN_HEIGHT-95)
    START_POSITION_PLAYER2 = (SCREEN_WIDTH-60, SCREEN_HEIGHT-95)
    

    # Obstacle and platform images
    PLATFORM = "assets\startpad.png"
    
    PLATFORM_PLAYER1_POS = (SCREEN_WIDTH-840, SCREEN_HEIGHT-50)
    PLATFORM_PLAYER2_POS = (SCREEN_WIDTH-60, SCREEN_HEIGHT-50)
    
    OBSTEACLE = "assets\obstacle.png"
    
    # Obstacle settings
    OBSTEACLE_SIZE = 100 
    OBSTEACLE_AMOUNT = 5
    
    
    
    # Spaceship settings
    FUEL = 100 
    GRAVITY = 10
    START_ANGLE = np.pi/2

    
    
    
   
    
    