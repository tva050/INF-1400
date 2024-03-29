""" 
Writen by: Trym Varland

module::  config.py
    This module contains the configuration of the game.
"""

import pygame
import os


""" _______CONFIG_______ """

pygame.font.init()

# Screen
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60 # Frames per second

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
FONT = pygame.font.Font(os.path.join("assets", "OriginTech personal use.ttf"), 40) # Font for the text in the game


# Background
BACKGROUND = pygame.image.load(os.path.join("assets", "space_background.jpg")).convert()
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() 


# Players spaceships
PLAYER1_IMG = os.path.join("assets", "spaceship1.png")  # Path to the image
PLAYER2_IMG = os.path.join("assets", "spaceship2.png")  # Path to the image
START_POSITION_PLAYER1 = (SCREEN_WIDTH-850, SCREEN_HEIGHT-90) # Position of the spaceship
START_POSITION_PLAYER2 = (SCREEN_WIDTH-50, SCREEN_HEIGHT-90)

SPACESHIP_SIZE = (90/1.5, 64/1.5) # Size of the spaceship
PLAYER1_IMG_LOADED = pygame.image.load(PLAYER1_IMG) # Load the image to use when rotating
PLAYER1_IMG_LOADED = pygame.transform.scale(PLAYER1_IMG_LOADED, SPACESHIP_SIZE).convert_alpha()
PLAYER1_THRUST     = pygame.image.load(os.path.join("assets", "thrust1_spaceship1.png")).convert_alpha()

PLAYER2_IMG_LOADED = pygame.image.load(PLAYER2_IMG) # Load the image to use when rotating
PLAYER2_IMG_LOADED = pygame.transform.scale(PLAYER2_IMG_LOADED, SPACESHIP_SIZE).convert_alpha()
PLAYER2_THRUST     = pygame.image.load(os.path.join("assets", "thrust1_spaceship2.png")).convert_alpha()

PLAYER_VELOCITY = 10 # Velocity of the spaceship
ROTATION_SPEED = 0.1 # Speed of the rotation
THRUST = 0.05 # Thrust of the spaceship


# Laser beam
PLAYER1_BEAM = os.path.join("assets", "player1_beam.png") # Path to the image of the laser beam
PLAYER2_BEAM = os.path.join("assets", "player2_beam.png") # Path to the image of the laser beam

BEAM_VELOCITY = 10 # Velocity of the laser beam
MAX_BEAMS = 3 # Maximum number of beams on the screen at the same time


# Platforms
PLATFORM_IMG  = os.path.join("assets", "platform.png") # Path to the image of the platform
PLATFORM_SIZE = (81.9, 64) # Size of the platform


PLATFORM_PLAYER1_POSITION = (START_POSITION_PLAYER1[0], START_POSITION_PLAYER1[1]+50) # Position of the platform
PLATFORM_PLAYER2_POSITION = (START_POSITION_PLAYER2[0], START_POSITION_PLAYER2[1]+50)


# Obstacles
OBSTACLE_IMG = os.path.join("assets", "obstacle.png")

OBSTACLE_SIZE = (90, 90)
OBSTACLE_POSITIONS = [(SCREEN_WIDTH-550, SCREEN_HEIGHT-250), (SCREEN_WIDTH-250, SCREEN_HEIGHT-150), (SCREEN_WIDTH-600, SCREEN_HEIGHT-100), (SCREEN_WIDTH-350, SCREEN_HEIGHT-400), (SCREEN_WIDTH-650, SCREEN_HEIGHT-500)]

# Score panel and won panel
SCORE_PANEL     = pygame.image.load(os.path.join("assets", "score_panel.png")) # Path to the image of the score panel
SCORE_PANEL     = pygame.transform.scale(SCORE_PANEL, (820/4, 280/5)).convert_alpha()
SCORE_PANEL_POS = (SCREEN_WIDTH/2-SCORE_PANEL.get_width()/2, 0)

GREEN_WON     = pygame.image.load(os.path.join("assets", "green_wins.png")) # Path to the image of the won panel
PURPLE_WON    = pygame.image.load(os.path.join("assets", "purple_wins.png"))
WON_PANEL_POS = (SCREEN_WIDTH/2-GREEN_WON.get_width()/2, SCREEN_HEIGHT/2-GREEN_WON.get_height()/2)

# MAIN MENU

MAYHEM      = pygame.image.load(os.path.join("assets", "mayham_start.png")).convert_alpha() # Game title image in main menu
PLAY_BUTTON = pygame.image.load(os.path.join("assets", "play_bottom.png")).convert_alpha() # Play button in main menu
INFO_BUTTON = pygame.image.load(os.path.join("assets", "info_bottom.png")).convert_alpha() # Info button in main menu

GREEN_CONTROLS  = pygame.image.load(os.path.join("assets", "green_controls.png")).convert_alpha() # Image with description of the controls
PURPLE_CONTROLS = pygame.image.load(os.path.join("assets", "purple_controls.png")).convert_alpha()
BACK_BUTTON     = pygame.image.load(os.path.join("assets", "back_bottom.png")).convert_alpha()
BACK_BUTTON     = pygame.transform.scale(BACK_BUTTON, (BACK_BUTTON.get_width()//2, BACK_BUTTON.get_height()//2)).convert_alpha()
POINT_INFO      = pygame.image.load(os.path.join("assets", "point_info.png")).convert_alpha() # Image with description of the points

# Settings
GRAVITY = FPS/5000 # Gravity of the game
MAX_FUEL = 100 # Maximum fuel of the spaceship
FUEL_CONSUMPTION = 0.1 # Fuel consumption of the spaceship
SCORE = 0 # Score of the game




