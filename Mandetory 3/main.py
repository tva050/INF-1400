import pygame

from config import Config
from spaceships import Spaceships
from obstecals import Obstacles
 
class Game:
    def __init__(self):
        self.player1 = Spaceships(Config.PLAYER1_IMG, Config.SCREEN, (0, 0))
        self.player2 = Spaceships(Config.PLAYER2_IMG, Config.SCREEN, (0, 0))
        
        self.players_spaceships = [self.player1, self.player2]
        self.spaceship_group = pygame.sprite.Group()
        for spaceship in self.players_spaceships:
            self.spaceship_group.add(spaceship)
            
        
       

        
    
        

    
    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            Config.SCREEN.blit(Config.BACKGROUND, (0, 0)) # Update background
            
            self.spaceship_group.draw(Config.SCREEN) # Update spaceship
           
            pygame.display.flip()
            pygame.display.update()
            
        
    