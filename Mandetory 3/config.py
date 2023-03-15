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
    
    screen_width = 900
    screen_height = 600
    
    screen = pygame.display.set_mode((screen_width, screen_height), 0)
    background = pygame.image.load("assets\space_background.jpg")
    background = pygame.transform.scale(background, (screen_width, screen_height)).convert()
    
    player1_img =  pygame.image.load("assets\player1.png")
    player1_img = pygame.transform.scale(player1_img, (12,12))
    player2_img =  pygame.image.load("assets\player2.png")
    player2_img = pygame.transform.scale(player2_img, (12,12))
    
    start_1 = pygame.image.load("assets\startpad.png")
    
    
    
    
   
    
    