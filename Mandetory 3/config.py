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
    
    # Screen size
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    
    # Screen size
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
    
    # Background image
    BACKGROUND = pygame.image.load("assets\space_background.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() 
    
    # Player images
    PLAYER1_IMG = "assets\player1.png" 
    PLAYER2_IMG = "assets\player2.png"
    PLAYER1_START_POSITION = (300, 700)
    PLAYER2_START_POSITION = (600, 700)
    

    # Obstacle and platform images
    PLATFORM = "assets\startpad.png"
    
    PLATFORM_PLAYER1_POS = (300, 700)
    PLATFORM_PLAYER2_POS = (600, 700)
    
    OBSTEACLE = "assets\obstacle.png"
    
    START_ANGLE = np.pi/2 
    
    OBSTEACLE_SIZE = 100 
    OBSTEACLE_AMOUNT = 5
    
    
    
    # Values
    FUEL = 100 
    GRAVITY = 10
    

    
    
    
   
    
    