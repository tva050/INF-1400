""" 
Writen by: Trym Varland
"""
import pygame, sys
import numpy as np
from pygame import Vector2 as Vec2
import math

""" _______CONFIG_______ """

pygame.font.init()

# Screen
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60 # Frames per second

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
FONT = pygame.font.Font("assets\OriginTech personal use.ttf", 40)


# Background
BACKGROUND = pygame.image.load("assets\space_background.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() 


# Players spaceships
PLAYER1_IMG = "assets\spaceship1.png"  # Path to the image
PLAYER2_IMG = "assets\spaceship2.png"
START_POSITION_PLAYER1 = (SCREEN_WIDTH-850, SCREEN_HEIGHT-90) # Position of the spaceship
START_POSITION_PLAYER2 = (SCREEN_WIDTH-50, SCREEN_HEIGHT-90)

SPACESHIP_SIZE = (90/1.5, 64/1.5) # Size of the spaceship
PLAYER1_IMG_LOADED = pygame.image.load(PLAYER1_IMG) # Load the image to use when rotating
PLAYER1_IMG_LOADED = pygame.transform.scale(PLAYER1_IMG_LOADED, SPACESHIP_SIZE).convert_alpha()
PLAYER1_THRUST = pygame.image.load(r"assets\thrust1_spaceship1.png").convert_alpha()

PLAYER2_IMG_LOADED = pygame.image.load(PLAYER2_IMG) # Load the image to use when rotating
PLAYER2_IMG_LOADED = pygame.transform.scale(PLAYER2_IMG_LOADED, SPACESHIP_SIZE).convert_alpha()
PLAYER2_THRUST = pygame.image.load(r"assets\thrust1_spaceship2.png").convert_alpha()

PLAYER_VELOCITY = 10 # Velocity of the spaceship
ROTATION_SPEED = 0.1 # Speed of the rotation
THRUST = 0.05 # Thrust of the spaceship


# Laser beam
PLAYER1_BEAM = "assets\player1_beam.png" # Path to the image of the laser beam
PLAYER2_BEAM = "assets\player2_beam.png"

BEAM_VELOCITY = 10 # Velocity of the laser beam
MAX_BEAMS = 3 # Maximum number of beams on the screen at the same time


# Platforms
PLATFORM_IMG = "assets\platform.png" # Path to the image of the platform
PLATFORM_SIZE = (81.9, 64) # Size of the platform


PLATFORM_PLAYER1_POSITION = (START_POSITION_PLAYER1[0], START_POSITION_PLAYER1[1]+50) # Position of the platform
PLATFORM_PLAYER2_POSITION = (START_POSITION_PLAYER2[0], START_POSITION_PLAYER2[1]+50)


# Obstacles
OBSTACLE_IMG = "assets\obstacle.png"

OBSTACLE_SIZE = (90, 90)

OBSTACLE_POSITIONS = [(SCREEN_WIDTH-550, SCREEN_HEIGHT-250), (SCREEN_WIDTH-250, SCREEN_HEIGHT-150), (SCREEN_WIDTH-600, SCREEN_HEIGHT-100), (SCREEN_WIDTH-350, SCREEN_HEIGHT-400), (SCREEN_WIDTH-650, SCREEN_HEIGHT-500)]

# Score panel and won panel
SCORE_PANEL = pygame.image.load("assets\score_panel.png")
SCORE_PANEL = pygame.transform.scale(SCORE_PANEL, (820/4, 280/5)).convert_alpha()
SCORE_PANEL_POS = (SCREEN_WIDTH/2-SCORE_PANEL.get_width()/2, 0)

GREEN_WON = pygame.image.load("assets\green_wins.png")
PURPLE_WON = pygame.image.load("assets\purple_wins.png")
WON_PANEL_POS = (SCREEN_WIDTH/2-GREEN_WON.get_width()/2, SCREEN_HEIGHT/2-GREEN_WON.get_height()/2)

# MAIN MENU

MAYHEM = pygame.image.load("assets\mayham_start.png").convert_alpha()
PLAY_BOTTOM = pygame.image.load("assets\play_bottom.png").convert_alpha()
INFO_BOTTOM = pygame.image.load("assets\info_bottom.png").convert_alpha()

GREEN_CONTROLS = pygame.image.load("assets\green_controls.png").convert_alpha()
PURPLE_CONTROLS = pygame.image.load("assets\purple_controls.png").convert_alpha()
BACK_BOTTOM = pygame.image.load(r"assets\back_bottom.png").convert_alpha()
BACK_BOTTOM = pygame.transform.scale(BACK_BOTTOM, (BACK_BOTTOM.get_width()//2, BACK_BOTTOM.get_height()//2)).convert_alpha()
POINT_INFO = pygame.image.load(r"assets\point_info.png").convert_alpha()

# Setting 
GRAVITY = FPS/5000 # Gravity of the game
MAX_FUEL = 100 # Maximum fuel of the spaceship
FUEL_CONSUMPTION = 0.1 # Fuel consumption of the spaceship
SCORE = 0 # Score of the game




