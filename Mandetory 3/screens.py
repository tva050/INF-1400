""" 
This is made mostly for fun, so alot of the code is from:
https://github.com/baraltech/Menu-System-PyGame/blob/551c6f3262cdb0d91b0803fa4a1beb8136c90bc1/main.py#L40

module:: screens.py
    This module contains the Screens class. This class is used to create the screens for the game.
"""

import pygame, sys
from config import *
from buttom import Buttom
from game import Game

class Screens:
    """ 
    This class is used to create the screens for the game.
    
    ...
    
    Attributes:
    ----------
    None
    
    Methods:
    -------
    info()
        Creates the info screen
    main_manu()
        Creates the main manu screen
    """
    def __init__(self):
        pass
    
    # def info(): and def main_manu(): is writen from 
    # https://github.com/baraltech/Menu-System-PyGame/blob/551c6f3262cdb0d91b0803fa4a1beb8136c90bc1/main.py#L40
    def info(self):
        """ 
        Creates the info screen.
        
        Parameters
        ----------
        None
        """
        pygame.display.set_caption("Info") # Sets the title of the window
        
        while True:
            SCREEN.blit(BACKGROUND, (0, 0))
            info_mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get(): # Checks for events
                if event.type == pygame.QUIT:
                    pygame.quit() # Quits the game
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN: # Checks if the mouse is clicked
                    if back_buttom.check_for_input(info_mouse_pos): # Checks if the back button is clicked go back to the main manu
                        self.main_manu(Screens)
            
            # Draws the info screen            
            green_controls = SCREEN.blit(GREEN_CONTROLS, (SCREEN_WIDTH/2-280, SCREEN_HEIGHT/2-250))
            green_spaceship = SCREEN.blit( pygame.image.load(PLAYER1_IMG), (SCREEN_WIDTH/2-220, SCREEN_HEIGHT/2+25))
            
            purple_controls = SCREEN.blit(PURPLE_CONTROLS, (SCREEN_WIDTH/2+20, SCREEN_HEIGHT/2-250))
            purple_spaceship = SCREEN.blit( pygame.image.load(PLAYER2_IMG), (SCREEN_WIDTH/2+150, SCREEN_HEIGHT/2+25))
            
            point_info = SCREEN.blit(POINT_INFO, (SCREEN_WIDTH/2-110, SCREEN_HEIGHT/2+30))
            
            back_buttom = Buttom(BACK_BUTTOM, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+250))
            back_buttom.draw(SCREEN)

            pygame.display.update()

    def main_manu(self): 
        """ 
        Creates the main manu screen.
        
        Parameters
        ----------
        None
        """
        pygame.display.set_caption("Main Menu")
        
        while True:
            SCREEN.blit(BACKGROUND, (0, 0))
            
            menu_mouse_pos = pygame.mouse.get_pos() # Gets the mouse position
            
            menu_img = MAYHEM # The image of the menu
            menu_rect = menu_img.get_rect(center = (SCREEN_WIDTH/2, 120)) # The rectangle of the menu
            SCREEN.blit(menu_img, menu_rect)
            
            # Creates the buttons
            play_buttom = Buttom(PLAY_BUTTOM, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-50))
            info_buttom = Buttom(INFO_BUTTOM, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50))
            
            
            for button in [play_buttom, info_buttom]: # Draws the buttons
                button.draw(SCREEN)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_buttom.check_for_input(menu_mouse_pos): # Checks if the play button is clicked and starts the game
                        Game().game_loop()
                    if info_buttom.check_for_input(menu_mouse_pos): # Checks if the info button is clicked and goes to the info screen
                        self.info(Screens)
                        
            pygame.display.update()
            
