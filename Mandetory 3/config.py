import pygame 

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
    pygame.font.init()
    
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
    BACKGROUND = "assets\space_background.jpg"
    """ BACKGROUND = pygame.image.load("assets\space_background.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() """
    
    PLAYER1_IMG = "assets\player1.png"
    PLAYER2_IMG = "assets\player2.png"
    """ PLAYER1_IMG =  pygame.image.load("assets\player1.png").convert_alpha()
    PLAYER1_IMG = pygame.transform.scale(PLAYER1_IMG, (71.9, 54))
    PLAYER2_IMG =  pygame.image.load("assets\player2.png").convert_alpha()
    PLAYER2_IMG = pygame.transform.scale(PLAYER2_IMG, (71.9, 54)) """
    
    PLATFORM = "assets\startpad.png"
    OBSTEACLE = "assets\obstacle.png"
    
    FUEL = 100 
    GRAVITY = 10
    
    
    
   
    
    