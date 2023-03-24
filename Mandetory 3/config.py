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
    START_POSITION_PLAYER1 = (SCREEN_WIDTH-880, SCREEN_HEIGHT-100)
    START_POSITION_PLAYER2 = (SCREEN_WIDTH-80, SCREEN_HEIGHT-100)
    
    SPACESHIP_SIZE = (90/1.5, 64/1.5)
    PLAYER_VELOCITY = 5
    ROTATION_SPEED = 5
    
    # Laser beam
    PLAYER1_BEAM = "assets\player1_beam.png"
    PLAYER2_BEAM = "assets\player2_beam.png"
    
    BEAM_VELOCITY = 7
    MAX_BEAMS = 3
   
    
    # Platforms
    PLATFORM_IMG = "assets\platform.png"
    
    PLATFORM_PLAYER1_POSITION = (START_POSITION_PLAYER1[0]+30, START_POSITION_PLAYER1[1]+60)
    PLATFORM_PLAYER2_POSITION = (START_POSITION_PLAYER2[0]+30, START_POSITION_PLAYER2[1]+60)
    
    # Obstacles
    OBSTACLE = "assets\obstacle.png"
    
    OBSTACLE_SIZE = (90, 90)
    
    OBSTACLE_POSITIONS = [(SCREEN_WIDTH-550, SCREEN_HEIGHT-250), (SCREEN_WIDTH-250, SCREEN_HEIGHT-150), (SCREEN_WIDTH-600, SCREEN_HEIGHT-100), (SCREEN_WIDTH-350, SCREEN_HEIGHT-400), (SCREEN_WIDTH-650, SCREEN_HEIGHT-500)]
    
    
    # Setting 
    GRAVITY = 10
    ANGLE = np.pi/2

    
    

   
    
    