import pygame

from config import Config
 
class Game:
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        Config.SCREEN.blit(Config.BACKGROUND, (0, 0)) # Update background
        
        Config.SCREEN.blit(Config.PLAYER1_IMG, (0, 0))
        Config.SCREEN.blit(Config.PLAYER2_IMG, (0, 0))

        pygame.display.update()
    