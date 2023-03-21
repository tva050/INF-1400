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
    pygame.display.set_caption("Shadow of the Moon")
    
    # Screen specifications
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    FPS = 60 # Frames per second
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
    
    OBSTACLE = "assets\obstacle.png"
    SEPERATION_OBSTACLE = r"assets\punktbilde.png"
    
    # Obstacle settings
    OBSTACLE_SIZE = (90, 90)
    # Make the asteroid be only between the start platforms, and 
    OBSTACLE_1_POS = (SCREEN_WIDTH-550, SCREEN_HEIGHT-250)
    OBSTACLE_2_POS = (SCREEN_WIDTH-250, SCREEN_HEIGHT-150)
    OBSTACLE_3_POS = (SCREEN_WIDTH-600, SCREEN_HEIGHT-100)
    OBSTACLE_4_POS = (SCREEN_WIDTH-350, SCREEN_HEIGHT-400)
    OBSTACLE_5_POS = (SCREEN_WIDTH-650, SCREEN_HEIGHT-500)
        
    # Spaceship settings
    FUEL = 100 
    GRAVITY = 10
    START_ANGLE = np.pi/2

    
    

   
    
    