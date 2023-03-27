import pygame, sys
import numpy as np
from pygame import Vector2 as Vec2
import math

""" _______CONFIG_______ """

class Config:
    pygame.display.set_caption("Mayhem")
    pygame.font.init()
    
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    FPS = 60 # Frames per second
    
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
    
    SCORE_FONT = pygame.font.Font("assets\OriginTech personal use.ttf", 40)
    WINNER_FONT = pygame.font.SysFont("STENCIL", 100)
    
    # Background
    BACKGROUND = pygame.image.load("assets\space_background.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() 
    
    # Players spaceships
    PLAYER1_IMG = "assets\spaceship1.png" 
    PLAYER2_IMG = "assets\spaceship2.png"
    START_POSITION_PLAYER1 = (SCREEN_WIDTH-850, SCREEN_HEIGHT-90)
    START_POSITION_PLAYER2 = (SCREEN_WIDTH-50, SCREEN_HEIGHT-90)
    
    SPACESHIP_SIZE = (90/1.5, 64/1.5)
    PLAYER1_IMG_LOADED = pygame.image.load(PLAYER1_IMG)
    PLAYER1_IMG_LOADED = pygame.transform.scale(PLAYER1_IMG_LOADED, SPACESHIP_SIZE).convert_alpha()
    
    PLAYER2_IMG_LOADED = pygame.image.load(PLAYER2_IMG)
    PLAYER2_IMG_LOADED = pygame.transform.scale(PLAYER2_IMG_LOADED, SPACESHIP_SIZE).convert_alpha()
    
    PLAYER1_THRUST = pygame.image.load(r"assets\ny_thrust.png").convert_alpha()
    PLAYER2_THRUST = pygame.image.load(r"assets\thrust_spaceship2.png")
    

    PLAYER2_THRUST = pygame.transform.scale(PLAYER2_THRUST, (SPACESHIP_SIZE)).convert_alpha()
    
    PLAYER_VELOCITY = 10
    ROTATION_SPEED = 0.1
    THRUST = 0.05
    
    # Laser beam
    PLAYER1_BEAM = "assets\player1_beam.png"
    PLAYER2_BEAM = "assets\player2_beam.png"
    
    BEAM_VELOCITY = 7
    MAX_BEAMS = 3
    
    
    # Platforms
    PLATFORM_IMG = "assets\platform.png"
    PLATFORM_SIZE = (81.9, 64)
    """ PLATFORM_PLAYER1_POSITION = (START_POSITION_PLAYER1[0]+30, START_POSITION_PLAYER1[1]+60)
    PLATFORM_PLAYER2_POSITION = (START_POSITION_PLAYER2[0]+30, START_POSITION_PLAYER2[1]+60) """
    
    PLATFORM_PLAYER1_POSITION = (START_POSITION_PLAYER1[0], START_POSITION_PLAYER1[1]+50)
    PLATFORM_PLAYER2_POSITION = (START_POSITION_PLAYER2[0], START_POSITION_PLAYER2[1]+50)
    
    # Obstacles
    OBSTACLE_IMG = "assets\obstacle.png"
    
    OBSTACLE_SIZE = (90, 90)
    
    OBSTACLE_POSITIONS = [(SCREEN_WIDTH-550, SCREEN_HEIGHT-250), (SCREEN_WIDTH-250, SCREEN_HEIGHT-150), (SCREEN_WIDTH-600, SCREEN_HEIGHT-100), (SCREEN_WIDTH-350, SCREEN_HEIGHT-400), (SCREEN_WIDTH-650, SCREEN_HEIGHT-500)]
    

    SCORE_PANEL = pygame.image.load("assets\score_panel.png")
    SCORE_PANEL = pygame.transform.scale(SCORE_PANEL, (820/4, 280/5)).convert_alpha()
    SCORE_PANEL_POS = (SCREEN_WIDTH/2-SCORE_PANEL.get_width()/2, 0)
    
    # Setting 
    GRAVITY = FPS/5000
    MAX_FUEL = 100
    FUEL_CONSUMPTION = 0.1
    SCORE = 0

    
    

   
    
    