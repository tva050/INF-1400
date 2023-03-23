import pygame 
import numpy as np
from pygame import Vector2 as Vec2
import math

""" _______CONFIG_______ """

class Config:
    pygame.display.set_caption("Mayhem")
    
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    FPS = 60 # Frames per second
    
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
    
    # Background
    BACKGROUND = pygame.image.load("assets\space_background.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() 
    
    # Players spaceships
    PLAYER1_IMG = "assets\spaceship1.png" 
    PLAYER2_IMG = "assets\spaceship2.png"
    START_POSITION_PLAYER1 = (SCREEN_WIDTH-880, SCREEN_HEIGHT-100)
    START_POSITION_PLAYER2 = (SCREEN_WIDTH-80, SCREEN_HEIGHT-100)
    
    SPACESHIP_SIZE = (90/1.5, 64/1.5)
    PLAYER_VELOCITY = 5
    ROTATION_SPEED = 5
    
    # Laser beam
    PLAYER1_BEAM = "assets\player1_beam.png"
    PLAYER2_BEAM = "assets\player2_beam.png"
    
    BEAM_VELOCITY = 10
    
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
    GRAVITY = 10
    ANGLE = np.pi/2

""" _______SPACESHIPS_______ """
class Spaceships(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, Config.SPACESHIP_SIZE).convert_alpha()
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        
        self.start_pos = position
        
        self.velocity = Vec2(0, 0)
        self.acceleration = 0 
        
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        
    
        self.clock = pygame.time.Clock()
        self.time = self.clock.tick(30)/1000 # Time in seconds
        
        self.screen = Config.SCREEN
        self.gravity = Config.GRAVITY
        
        self.laserbeam_group = pygame.sprite.Group()
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
        
    def shoot(self, image):
        laserbeam = LaserBeam(image, self.rect.center)
        self.laserbeam_group.add(laserbeam)                
    
    def spaceship_boundaries(self):
        if self.rect.x  > Config.SCREEN_WIDTH:
            self.velocity.x = -1
        elif self.rect.x < 0:
            self.velocity.x = 1
        elif self.rect.y > Config.SCREEN_HEIGHT - self.image_height:
            self.velocity.y = -1
        elif self.rect.y < 0:   
            self.velocity.y = 1
        
    def move(self, dx, dy):
        self.rect.x += dx + self.acceleration * self.time
        self.rect.y += dy + self.acceleration * self.time
        
    def thrust(self, velocity):
        self.velocity.y = -velocity
    def move_right(self, velocity):
        self.velocity.x = velocity 
    def move_left(self, velocity):
        self.velocity.x = -velocity
    
    def update(self):
        self.move(self.velocity.x, self.velocity.y)
        self.spaceship_boundaries() 
        
        self.velocity.y += min(1, self.gravity)
        self.velocity.x = 0
    
        self.draw()

    def reset(self):
        self.rect.x = self.start_pos[0]
        self.rect.y = self.start_pos[1]
        self.velocity = Vec2(0, 0)
        self.acceleration = 0
        self.rect.centerx = self.start_pos[0]
        self.rect.centery = self.start_pos[1]
    

""" _______LASER_BEAM_______ """
class LaserBeam(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (20, 20)).convert_alpha()
        
        self.position = position
        self.velocity = Config.BEAM_VELOCITY
        
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

        self.screen = Config.SCREEN
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    def move(self):
        self.rect.x += self.velocity
        self.rect.y += self.velocity
        
    def update(self):
        self.move()
        self.draw()
    
   

""" _______PLATFORMS_______ """

class Platforms(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(Config.PLATFORM_IMG)
        self.image = pygame.transform.scale(self.image, (81.9, 64)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.screen = Config.SCREEN
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.draw()
        

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, Config.OBSTACLE_SIZE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [position[0], position[1]]
        self.screen = Config.SCREEN
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.draw()

""" _______GAME_______ """

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        
        # Spaceships
        self.player1_spaceship = Spaceships(Config.PLAYER1_IMG, Config.START_POSITION_PLAYER1)
        self.player2_spaceship = Spaceships(Config.PLAYER2_IMG, Config.START_POSITION_PLAYER2)
        self.spaceship_group = pygame.sprite.Group()
        for spaceship in self.player1_spaceship, self.player2_spaceship:
            self.spaceship_group.add(spaceship)
        
        self.player1_platform = Platforms(Config.PLATFORM_PLAYER1_POSITION[0], Config.PLATFORM_PLAYER1_POSITION[1])
        self.player2_platform = Platforms(Config.PLATFORM_PLAYER2_POSITION[0], Config.PLATFORM_PLAYER2_POSITION[1])
        self.platform_group = pygame.sprite.Group()
        for platform in self.player1_platform, self.player2_platform:
            self.platform_group.add(platform)
            
        self.obstacle1 = Obstacles(Config.OBSTACLE, Config.OBSTACLE_1_POS)
        self.obstacle2 = Obstacles(Config.OBSTACLE, Config.OBSTACLE_2_POS)
        self.obstacle3 = Obstacles(Config.OBSTACLE, Config.OBSTACLE_3_POS)
        self.obstacle4 = Obstacles(Config.OBSTACLE, Config.OBSTACLE_4_POS)
        self.obstacle5 = Obstacles(Config.OBSTACLE, Config.OBSTACLE_5_POS)
        self.obstacle_group = pygame.sprite.Group()
        for obstacle in self.obstacle1, self.obstacle2, self.obstacle3, self.obstacle4, self.obstacle5:
            self.obstacle_group.add(obstacle)

        
    def draw(self):
        Config.SCREEN.blit(Config.BACKGROUND, (0, 0))
        
        self.spaceship_group.draw(Config.SCREEN)
        self.platform_group.draw(Config.SCREEN)
        self.obstacle_group.draw(Config.SCREEN)
        
    
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
            
        if keys[pygame.K_SPACE]:
            self.player1_spaceship.shoot(Config.PLAYER1_BEAM)
        if keys[pygame.K_LSHIFT]:
            self.player2_spaceship.shoot(Config.PLAYER2_BEAM)
    
    def collision_platform(self):
        if pygame.sprite.collide_rect(self.player1_spaceship, self.player1_platform):
            self.player1_spaceship.velocity.y = 0
            self.player1_spaceship.rect.bottom = self.player1_platform.rect.top
        if pygame.sprite.collide_rect(self.player2_spaceship, self.player2_platform):
            self.player2_spaceship.velocity.y = 0
            self.player2_spaceship.rect.bottom = self.player2_platform.rect.top
    
    def collision_obstacles(self):
        for obstacle in self.obstacle_group:
            if pygame.sprite.collide_rect(self.player1_spaceship, obstacle):
                self.player1_spaceship.reset()
            if pygame.sprite.collide_rect(self.player2_spaceship, obstacle):
                self.player2_spaceship.reset()
            
    def collision(self):
        self.collision_platform()
        self.collision_obstacles()
    
    def update(self):
        self.spaceship_group.update()
        self.platform_group.update()
        self.obstacle_group.update()

 
    
    def game_loop(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            self.clock.tick(Config.FPS)
            
            self.event_handler()
            self.collision()
            self.update()
            self.draw()
            
            pygame.display.update()



if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.game_loop()

        
        
        