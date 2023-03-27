""" 
Writen by: Trym Varland

module:: game.py
    This module contains the Game class, which is the main class of the game. 
    It contains the game loop and the event handler.
"""
import pygame
from config import *
from spaceships import Spaceships
from laserbeam import LaserBeam
from platforms import Platforms
from obstacles import Obstacles



""" _______GAME_______ """

class Game:
    """ 
    Class which is the main class of the game. It contains the game loop and the event handler.
    
    ...
    
    Attributes
    ----------
    clock : pygame.time.Clock
        The clock of the game
    player1_spaceship : Spaceships  
        The spaceship of player 1
    player2_spaceship : Spaceships
        The spaceship of player 2
    spaceship_group : pygame.sprite.Group
        The group of the spaceships
    player1_platform : Platforms
        The platform of player 1
    player2_platform : Platforms
        The platform of player 2
    platform_group : pygame.sprite.Group
        The group of the platforms
    obstacle_group : pygame.sprite.Group
        The group of the obstacles
    laserbeam_group : pygame.sprite.Group
        The group of the laserbeams
    
    Methods
    -------
    event_handler()
        The event handler of the game
    shoot_keys()
        The keys for shooting
    hit_by_beam()
        Checks if the spaceship is hit by a laserbeam
    collision_between_spaceships()
        Checks if the spaceships collide with each other
    collision_platforms()
        Checks if the spaceships collide with the platforms
    collision_obstacles()
        Checks if the spaceships collide with the obstacles
    fuel_bar()
        Draws the fuel bar
    score()
        Draws the score
    reset_handler()
        Resets the game by pressing the SPACE key
    draw_winner()
        Draws the winner window
    collision()
        Checks if the spaceships collide with something
    draw()
        Draws the game
    update()
        Updates the game
    
    game_loop()
        The game loop of the game
    """
    def __init__(self):
        """ 
        Constructs all the necessary attributes for the game object.
        
        Parameters
        ----------
            None
        """
        self.clock = pygame.time.Clock()
    
        # Spaceships
        self.player1_spaceship = Spaceships(PLAYER1_IMG, START_POSITION_PLAYER1, (0,0))
        self.player2_spaceship = Spaceships(PLAYER2_IMG, START_POSITION_PLAYER2, (0,0))
        self.spaceship_group = pygame.sprite.Group() # Group of the spaceships
        for spaceship in self.player1_spaceship, self.player2_spaceship:
            self.spaceship_group.add(spaceship)
        
        # Platforms
        self.player1_platform = Platforms(PLATFORM_PLAYER1_POSITION[0], PLATFORM_PLAYER1_POSITION[1])
        self.player2_platform = Platforms(PLATFORM_PLAYER2_POSITION[0], PLATFORM_PLAYER2_POSITION[1])
        self.platform_group = pygame.sprite.Group() # Group of the platforms
        for platform in self.player1_platform, self.player2_platform:
            self.platform_group.add(platform)
            
        # Obstacles
        self.obstacle_group = pygame.sprite.Group() # Group of the obstacles
        for positions in range(len(OBSTACLE_POSITIONS)): # Gives the index of the list
            obstacle = Obstacles(OBSTACLE_IMG, OBSTACLE_POSITIONS[positions])
            self.obstacle_group.add(obstacle)
        
        # Player 1 controls
    def event_handler(self):
        """
        The event handler of the game.
        
        Parameters
        ----------
            None
        """
        keys = pygame.key.get_pressed()
        
        # Player 1 controls
        if keys[pygame.K_w] and self.player1_spaceship.rect.y > 0: # If the player presses the W key and the spaceship is not at the top of the screen
            self.player1_spaceship.image = pygame.transform.rotate(PLAYER1_THRUST, self.player1_spaceship.angle) # Rotate the image of the spaceship and set it to the thrust image
            self.player1_spaceship.thrust() # Thrust the spaceship
        if keys[pygame.K_d] and self.player1_spaceship.rect.x < SCREEN_WIDTH - self.player1_spaceship.image_width: # If the player presses the D key and the spaceship is not at the right side of the screen
            self.player1_spaceship.image, self.player1_spaceship.rect = self.player1_spaceship.move_right(PLAYER1_IMG_LOADED) # Move the spaceship to the right
        if keys[pygame.K_a] and self.player1_spaceship.rect.x > 0:  # If the player presses the A key and the spaceship is not at the left side of the screen
            self.player1_spaceship.image, self.player1_spaceship.rect = self.player1_spaceship.move_left(PLAYER1_IMG_LOADED) # Move the spaceship to the left
        if keys[pygame.K_w] == False: # If the player does not press the W key
            self.player1_spaceship.image = pygame.transform.rotate(PLAYER1_IMG_LOADED, self.player1_spaceship.angle) # Rotate the image and set it to the original image
        
        # Player 2 controls
        if keys[pygame.K_UP] and self.player2_spaceship.rect.y > 0:
            self.player2_spaceship.image = pygame.transform.rotate(PLAYER2_THRUST, self.player2_spaceship.angle)
            self.player2_spaceship.thrust()
        if keys[pygame.K_RIGHT] and self.player2_spaceship.rect.x < SCREEN_WIDTH - self.player2_spaceship.image_width:
            self.player2_spaceship.image, self.player2_spaceship.rect = self.player2_spaceship.move_right(PLAYER2_IMG_LOADED)
        if keys[pygame.K_LEFT] and self.player2_spaceship.rect.x > 0:
            self.player2_spaceship.image, self.player2_spaceship.rect = self.player2_spaceship.move_left(PLAYER2_IMG_LOADED)
        if keys[pygame.K_UP] == False:
            self.player2_spaceship.image = pygame.transform.rotate(PLAYER2_IMG_LOADED, self.player2_spaceship.angle)
            
        # Shoot
    def shootkeys(self, spaceship):
        """ 
        The keys for shooting.
    
        Parameters
        ----------
        spaceship : Spaceships
            The spaceship of the player who is shooting
        """
        keys = pygame.key.get_pressed()
        if spaceship == self.player1_spaceship: # If the spaceship is the player 1 spaceship
            if keys[pygame.K_LCTRL]: # If the player presses the LCTRL key
                if self.player1_spaceship.shoot_cooldown == 0: # If the cooldown is 0
                    self.player1_spaceship.shoot_cooldown = 20 # Set the cooldown to 20
                    spaceship.beams.add(LaserBeam(PLAYER1_BEAM, (spaceship.rect.centerx, spaceship.rect.centery), self.player1_spaceship.angle)) # Add a laser beam to the spaceship
        elif spaceship == self.player2_spaceship:
            if keys[pygame.K_RCTRL]:
                if self.player2_spaceship.shoot_cooldown == 0:
                    self.player2_spaceship.shoot_cooldown = 20
                    spaceship.beams.add(LaserBeam(PLAYER2_BEAM, (spaceship.rect.centerx, spaceship.rect.centery), self.player2_spaceship.angle))

    def shoot(self):
        self.shootkeys(self.player1_spaceship)
        self.shootkeys(self.player2_spaceship)

    def hit_by_beam(self):
        """ 
        Checks if the spaceship is hit by a beam.
    
        Parameters
        ----------
            None
        """
        if pygame.sprite.spritecollide(self.player1_spaceship, self.player2_spaceship.beams, True):
            self.player2_spaceship.score += 1 # Add 1 to the score of player 2
        if pygame.sprite.spritecollide(self.player2_spaceship, self.player1_spaceship.beams, True):
            self.player1_spaceship.score += 1 
    
    def collison_between_spaceships(self):
        """ 
        Checks if the spaceships collide with each other.
        
        Parameters
        ----------
            None
        """
        if pygame.sprite.collide_mask(self.player1_spaceship, self.player2_spaceship): # If the spaceships collide they both lose 1 score and get reset
            self.player1_spaceship.reset() 
            self.player2_spaceship.reset()
            self.player1_spaceship.score -= 1
            self.player2_spaceship.score -= 1
            
    def collision_platform(self):
        """ 
        Checks if the spaceships collide with the platforms.
    
        Parameters
        ----------
            None
        """
        for platform in self.platform_group:
            # If the spaceship collides with the platform and the spaceship is falling down then set the velocity to 0 and set the top of the spaceship to the bottom of the platform
            if pygame.sprite.collide_rect(self.player1_spaceship, platform) and self.player1_spaceship.velocity.y > 0:
                self.player1_spaceship.velocity.y = 0
                self.player1_spaceship.rect.top= platform.rect.bottom
                self.player1_spaceship.fuel = MAX_FUEL
            if pygame.sprite.collide_rect(self.player2_spaceship, platform) and self.player2_spaceship.velocity.y > 0:
                self.player2_spaceship.velocity.y = 0
                self.player2_spaceship.rect.bottom = platform.rect.top
                self.player2_spaceship.fuel = MAX_FUEL
               
        
    def collision_obstacles(self):
        """  
        Checks if the spaceships collide with the obstacles.
        
        Parameters
        ----------
            None
        """
        for obstacle in self.obstacle_group:
            if pygame.sprite.collide_mask(self.player1_spaceship, obstacle): # If the spaceship collides with the obstacle then reset the spaceship and subtract 1 from the score
                self.player1_spaceship.reset()
                self.player1_spaceship.score -= 1
            if pygame.sprite.collide_mask(self.player2_spaceship, obstacle):
                self.player2_spaceship.reset()
                self.player2_spaceship.score -= 1
        # laserbeam collision with obstacles -> destroy laserbeam (dokill = False, dokill2 = True)
        if pygame.sprite.groupcollide(self.obstacle_group, self.player1_spaceship.beams, False, True): # If the laserbeam collides with the obstacle then destroy the laserbeam
            pass
        if pygame.sprite.groupcollide(self.obstacle_group, self.player2_spaceship.beams, False, True):
            pass
        
    def fuel_bar(self):
        """ 
        Draws the fuel bar.
        
        Parameters
        ----------
            None
        """    
        pygame.draw.rect(SCREEN, (47,150,39,255), (0, SCREEN_HEIGHT-10, self.player1_spaceship.fuel, 10))
        pygame.draw.rect(SCREEN, (148,85,194,255), (SCREEN_WIDTH-self.player2_spaceship.fuel, SCREEN_HEIGHT-10, self.player2_spaceship.fuel, 10))
        
    def score(self):
        """ 
        Draws the score.
        
        Parameters
        ----------
            None
        """
        SCREEN.blit(SCORE_PANEL, SCORE_PANEL_POS)
        SCREEN.blit(FONT.render(str(self.player1_spaceship.score), True, (255,255,255)), (SCREEN_WIDTH/2-60, 10))
        SCREEN.blit(FONT.render(str(self.player2_spaceship.score), True, (255,255,255)), (SCREEN_WIDTH/2+50, 10))

               
    def draw_winner(self):
        """ 
        Draws the winner.
    
        Parameters
        ----------
            None
        """
        if self.player1_spaceship.score == 5: # If the score of player 1 is 1 then draw the green won panel and reset the game
            SCREEN.blit(GREEN_WON, (WON_PANEL_POS))
            self.reset_handler()
        elif self.player2_spaceship.score == 5:
            SCREEN.blit(PURPLE_WON, (WON_PANEL_POS))
            self.reset_handler()
        pygame.display.update()
        
        
        
    def reset_handler(self):
        """ 
        Resets the game.
        
        Parameters
        ----------
            None
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]: # If the spacebar is pressed then reset the game
                self.player1_spaceship.reset()
                self.player2_spaceship.reset()
                self.player1_spaceship.score = 0
                self.player2_spaceship.score = 0 
                self.player1_spaceship.beams.empty() # Empty the laserbeams so they don't get drawn again when the game is reset
                self.player2_spaceship.beams.empty() 
                    
            
    def collision(self):
        """ 
        Checks for collisions.
        
        Parameters
        ----------
            None
        """
        self.collision_platform()
        self.collision_obstacles()
        self.collison_between_spaceships()
        self.hit_by_beam()
        
   
    def update(self):
        """ 
        Updates the game.
        
        Parameters
        ----------
            None
        """
        self.spaceship_group.update()
        self.platform_group.update()
        self.obstacle_group.update()
        self.player1_spaceship.beams.update()
        self.player2_spaceship.beams.update()
        
        
    def draw(self):
        """ 
        Draws the game.
        
        Parameters
        ----------
            None
        """
        SCREEN.blit(BACKGROUND, (0, 0))
        
        self.player1_spaceship.beams.draw(SCREEN)
        self.player2_spaceship.beams.draw(SCREEN)
        self.spaceship_group.draw(SCREEN)
        self.platform_group.draw(SCREEN)
        self.obstacle_group.draw(SCREEN)  
        self.fuel_bar()  
        self.score()
        
        pygame.display.update()
        
        
    def game_loop(self):
        pygame.display.set_caption("Mayhem") # Title of the game window
        pygame.init()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If the quit button is pressed then quit the game
                    run = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # If the escape key is pressed then quit the game
                        run = False
                        break
                
                
            if self.player1_spaceship.score == 5 or self.player2_spaceship.score == 5: # If the score of one of the players is a given score then draw the winner
                self.draw_winner()
                self.clock.tick(FPS)
                continue 
            
               
                
            self.clock.tick(FPS)
            
            self.event_handler()
            self.shoot()
            self.collision()
            self.update()
            self.draw()
            
            
            
            pygame.display.update()

        pygame.quit()
    

