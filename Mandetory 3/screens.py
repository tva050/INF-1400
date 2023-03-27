""" 
This is made mostly for fun, so alot of the code is from:
https://github.com/baraltech/Menu-System-PyGame/blob/551c6f3262cdb0d91b0803fa4a1beb8136c90bc1/main.py#L40
"""

import pygame
from config import *
from bottom_ import Bottom
from main_game import Game

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
                    if back_bottom.check_for_input(info_mouse_pos): # Checks if the back button is clicked go back to the main manu
                        self.main_manu(Screens)
            
            # Draws the info screen            
            green_controls = SCREEN.blit(GREEN_CONTROLS, (SCREEN_WIDTH/2-280, SCREEN_HEIGHT/2-250))
            green_spaceship = SCREEN.blit( pygame.image.load(PLAYER1_IMG), (SCREEN_WIDTH/2-220, SCREEN_HEIGHT/2+25))
            
            purple_controls = SCREEN.blit(PURPLE_CONTROLS, (SCREEN_WIDTH/2+20, SCREEN_HEIGHT/2-250))
            purple_spaceship = SCREEN.blit( pygame.image.load(PLAYER2_IMG), (SCREEN_WIDTH/2+150, SCREEN_HEIGHT/2+25))
            
            point_info = SCREEN.blit(POINT_INFO, (SCREEN_WIDTH/2-110, SCREEN_HEIGHT/2+30))
            
            back_bottom = Bottom(BACK_BOTTOM, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+250))
            back_bottom.draw(SCREEN)

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
            play_bottom = Bottom(PLAY_BOTTOM, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-50))
            info_bottom = Bottom(INFO_BOTTOM, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50))
            
            
            for button in [play_bottom, info_bottom]: # Draws the buttons
                button.draw(SCREEN)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_bottom.check_for_input(menu_mouse_pos): # Checks if the play button is clicked and starts the game
                        Game().game_loop()
                    if info_bottom.check_for_input(menu_mouse_pos): # Checks if the info button is clicked and goes to the info screen
                        self.info(Screens)
                        
            pygame.display.update()
            
