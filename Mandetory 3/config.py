import pygame 
import numpy as np
from pygame import Vector2 as Vec2
import math

""" _______CONFIG_______ """

class Config:
    pygame.display.set_caption("Mayhem")
    
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    FPS = 60 # Frames per second
    
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
    # Background
    BACKGROUND = pygame.image.load("assets\space_background.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() 
    
    # Players spaceships
    PLAYER1_IMG = "assets\spaceship1.png" 
    PLAYER2_IMG = "assets\spaceship2.png"
    START_POSITION_PLAYER1 = (SCREEN_WIDTH-, SCREEN_HEIGHT-95)
    START_POSITION_PLAYER2 = (820, SCREEN_HEIGHT-95)
    
    SPACESHIP_SIZE = (90/1.5, 64/1.5)
    PLAYER_VELOCITY = 5
    ROTATION_SPEED = 5
    
    # Platforms
    PLATFORM_IMG = "assets\platform.png"
    
    PLATFORM_PLAYER1_POSITION = (SCREEN_WIDTH-880, SCREEN_HEIGHT-50)
    PLATFORM_PLAYER2_POSITION = (SCREEN_WIDTH-90, SCREEN_HEIGHT-50)
    
    # Obstacles
    OBSTACLE = "assets\obstacle.png"
    
    OBSTACLE_SIZE = (90, 90)
    
    # Make the asteroid be only between the start platforms, and 
    OBSTACLE_1_POS = (SCREEN_WIDTH-550, SCREEN_HEIGHT-250)
    OBSTACLE_2_POS = (SCREEN_WIDTH-250, SCREEN_HEIGHT-150)
    OBSTACLE_3_POS = (SCREEN_WIDTH-600, SCREEN_HEIGHT-100)
    OBSTACLE_4_POS = (SCREEN_WIDTH-350, SCREEN_HEIGHT-400)
    OBSTACLE_5_POS = (SCREEN_WIDTH-650, SCREEN_HEIGHT-500)
    
    # Setting 
    GRAVITY = 10
    ANGLE = np.pi/2

    
    

   
    
    