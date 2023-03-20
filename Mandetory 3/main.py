import pygame
import random

from config import Config
from spaceships import Spaceships
from platform_1 import Platform
from obstecals import Obstacles


class Game:
    def __init__(self):
        
        # Spaceships
        self.player1_spaceship = Spaceships(Config.PLAYER1_IMG, Config.START_POSITION_PLAYER1)
        self.player2_spaceship = Spaceships(Config.PLAYER2_IMG, Config.START_POSITION_PLAYER2)
        self.spaceship_group = pygame.sprite.Group()
        for spaceship in self.player1_spaceship, self.player2_spaceship:
            self.spaceship_group.add(spaceship)
        
        # Platforms
        self.platform_1 = Platform(Config.PLATFORM_PLAYER1_POS[0], Config.PLATFORM_PLAYER1_POS[1])
        self.platform_2 = Platform(Config.PLATFORM_PLAYER2_POS[0], Config.PLATFORM_PLAYER2_POS[1])
        self.platform_group = pygame.sprite.Group()
        for platform in self.platform_1, self.platform_2:
            self.platform_group.add(platform)
            
        # Obstacles
        self.obstacle_group = pygame.sprite.Group()
        for _ in range(Config.NUMBER_OF_OBSTACLES):
            self.obstacle_group.add(Obstacles(Config.OBSTACLE,random.randint(0, Config.OBSTACLE_AREA[0]), random.randint(0, Config.OBSTACLE_AREA[1])))
        self.obstacle_group.add(Obstacles(Config.SEPERATION_OBSTACLE, Config.SEPERATION_OBSTACLE_POSITON[0], Config.SEPERATION_OBSTACLE_POSITON[1])) 
            
    
        

    
    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            Config.SCREEN.blit(Config.BACKGROUND, (0, 0)) # Update background
            
            
            self.platform_group.draw(Config.SCREEN) # Update platform
            self.spaceship_group.draw(Config.SCREEN) # Update spaceship
            self.obstacle_group.draw(Config.SCREEN) # Update obstacle
            
            pygame.display.update()

        
    