import pygame, sys
import numpy as np
from pygame import Vector2 as Vec2
import math

""" _______CONFIG_______ """

class Config:
    pygame.display.set_caption("Mayhem")
    pygame.font.init()
    
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    FPS = 60 # Frames per second
    
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
    
    SCORE_FONT = pygame.font.SysFont("comicsans", 40)
    
    # Background
    BACKGROUND = pygame.image.load("assets\space_background.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() 
    
    # Players spaceships
    PLAYER1_IMG = "assets\spaceship1.png" 
    PLAYER2_IMG = "assets\spaceship2.png"
    PLAYER2_IMG_LOADED = pygame.image.load(PLAYER2_IMG)
    START_POSITION_PLAYER1 = (SCREEN_WIDTH-880, SCREEN_HEIGHT-100)
    START_POSITION_PLAYER2 = (SCREEN_WIDTH-80, SCREEN_HEIGHT-100)
    
    SPACESHIP_SIZE = (90/1.5, 64/1.5)
    PLAYER1_IMG_LOADED = pygame.image.load(PLAYER1_IMG)
    PLAYER1_IMG_LOADED = pygame.transform.scale(PLAYER1_IMG_LOADED, SPACESHIP_SIZE).convert_alpha()
    PLAYER2_IMG_LOADED = pygame.image.load(PLAYER2_IMG)
    PLAYER2_IMG_LOADED = pygame.transform.scale(PLAYER2_IMG_LOADED, SPACESHIP_SIZE).convert_alpha()
    PLAYER_VELOCITY = 100
    ROTATION_SPEED = 0.1
    THRUST = 0.2
    
    # Laser beam
    PLAYER1_BEAM = "assets\player1_beam.png"
    PLAYER2_BEAM = "assets\player2_beam.png"
    
    BEAM_VELOCITY = 7
    MAX_BEAMS = 3
    
    
    # Platforms
    PLATFORM_IMG = "assets\platform.png"
    
    PLATFORM_PLAYER1_POSITION = (START_POSITION_PLAYER1[0]+30, START_POSITION_PLAYER1[1]+60)
    PLATFORM_PLAYER2_POSITION = (START_POSITION_PLAYER2[0]+30, START_POSITION_PLAYER2[1]+60)
    
    # Obstacles
    OBSTACLE = "assets\obstacle.png"
    
    OBSTACLE_SIZE = (90, 90)
    
    # Make the asteroid be only between the start platforms, and 
    OBSTACLE_1_POS = (SCREEN_WIDTH-550, SCREEN_HEIGHT-250)
    OBSTACLE_2_POS = (SCREEN_WIDTH-250, SCREEN_HEIGHT-150)
    OBSTACLE_3_POS = (SCREEN_WIDTH-600, SCREEN_HEIGHT-100)
    OBSTACLE_4_POS = (SCREEN_WIDTH-350, SCREEN_HEIGHT-400)
    OBSTACLE_5_POS = (SCREEN_WIDTH-650, SCREEN_HEIGHT-500)
    
    # Setting 
    GRAVITY = FPS/1000
    SCORE = 0
    

""" _______SPACESHIPS_______ """
class Spaceships(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, Config.SPACESHIP_SIZE).convert_alpha()
        self.image_width, self.image_height = self.image.get_size()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.start_pos = position
        self.speed = Vec2(speed)
        self.position = Vec2(position)
        self.angle = np.degrees(0)
        
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
    
    def move(self):
        self.position += self.speed 
        self.speed += Vec2(0, Config.GRAVITY)
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
        
    def thrust(self):
        thrust_vector = Vec2(0, Config.THRUST)
        thrust_vector.rotate_ip(-self.angle+180)
        self.speed += thrust_vector
        
    def move_right(self, image):
        self.angle -= np.degrees(Config.ROTATION_SPEED)
        rot_image = pygame.transform.rotate(image, self.angle)
        rot_rec = rot_image.get_rect(center = self.rect.center)
        return rot_image, rot_rec
    
    def move_left(self, image):
        self.angle += np.degrees(Config.ROTATION_SPEED)
        rot_image = pygame.transform.rotate(image, self.angle)
        rot_rec = rot_image.get_rect(center = self.rect.center)
        return rot_image, rot_rec
    
    def update(self):
        self.move()
        


class Game:
    def __init__(self):
        self.player1_spaceship = Spaceships(Config.PLAYER1_IMG, Config.START_POSITION_PLAYER1, (0, 0))
        self.player2_spaceship = Spaceships(Config.PLAYER2_IMG, Config.START_POSITION_PLAYER2, (0, 0))
        self.spaceships = pygame.sprite.Group()
        for spaceship in [self.player1_spaceship, self.player2_spaceship]:
            self.spaceships.add(spaceship)
    
    def event_management(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player1_spaceship.rect.y > 0:
            self.player1_spaceship.image, self.player1_spaceship.rect = self.player1_spaceship.move_left(Config.PLAYER1_IMG_LOADED)
        if keys[pygame.K_RIGHT] and self.player1_spaceship.rect.y > 0:
            self.player1_spaceship.image, self.player1_spaceship.rect = self.player1_spaceship.move_right(Config.PLAYER1_IMG_LOADED)
        if keys[pygame.K_UP] and self.player1_spaceship.rect.y > 0:
            self.player1_spaceship.thrust()
            
        if keys[pygame.K_a] and self.player2_spaceship.rect.y > 0:
            self.player2_spaceship.image, self.player2_spaceship.rect = self.player2_spaceship.move_left(Config.PLAYER2_IMG_LOADED)
        if keys[pygame.K_d] and self.player2_spaceship.rect.y > 0:
            self.player2_spaceship.image, self.player2_spaceship.rect = self.player2_spaceship.move_right(Config.PLAYER2_IMG_LOADED)
        if keys[pygame.K_w] and self.player2_spaceship.rect.y > 0:
            self.player2_spaceship.thrust()
    
    def draw(self):
        Config.SCREEN.blit(Config.BACKGROUND, (0, 0))
        self.spaceships.draw(Config.SCREEN)
    
    def update(self):
        self.spaceships.update()
 
    
    def game_loop(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        break
                    
                    
            clock.tick(Config.FPS)
            
            
            self.event_management()
            self.update()
            self.draw()
            
            pygame.display.update()
            
            
if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.game_loop()
    
            
            
        
