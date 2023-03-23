import pygame

from config import Config
from spaceships import Spaceships

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        
        # Spaceships
        self.player1_spaceship = Spaceships(Config.PLAYER1_IMG, Config.START_POSITION_PLAYER1)
        self.player2_spaceship = Spaceships(Config.PLAYER2_IMG, Config.START_POSITION_PLAYER2)
        
        self.spaceship_group = pygame.sprite.Group()
        self.spaceship_group.add(self.player1_spaceship)
        self.spaceship_group.add(self.player2_spaceship)
    
    def draw(self):
        Config.SCREEN.blit(Config.BACKGROUND, (0, 0))
        self.player1_spaceship.draw()
        self.player2_spaceship.draw()
        
        pygame.display.update()
        
    def event_handler(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.player1_spaceship.thrust(Config.PLAYER_VELOCITY)
        if keys[pygame.K_RIGHT]:
            self.player1_spaceship.move_right(Config.PLAYER_VELOCITY)
        if keys[pygame.K_LEFT]:
            self.player1_spaceship.move_left(Config.PLAYER_VELOCITY)
        
        if keys[pygame.K_w]:
            self.player2_spaceship.thrust(Config.PLAYER_VELOCITY)
        if keys[pygame.K_d]:
            self.player2_spaceship.move_right(Config.PLAYER_VELOCITY)
        if keys[pygame.K_a]:
            self.player2_spaceship.move_left(Config.PLAYER_VELOCITY)
        
    
    def update(self):
        self.player1_spaceship.update()
        self.player2_spaceship.update()
        
    
    def game_loop(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            self.clock.tick(Config.FPS)
            
            self.event_handler()
            self.update()
            self.draw()
            
            pygame.display.update()

        
    

        
    