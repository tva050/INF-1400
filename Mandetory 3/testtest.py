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
    
    SCORE_FONT = pygame.font.SysFont("STENCIL", 45)
    
    # Background
    BACKGROUND = pygame.image.load("assets\space_background.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() 
    
    # Players spaceships
    PLAYER1_IMG = "assets\spaceship1.png" 
    PLAYER2_IMG = "assets\spaceship2.png"
    START_POSITION_PLAYER1 = (SCREEN_WIDTH-850, SCREEN_HEIGHT-90)
    START_POSITION_PLAYER2 = (SCREEN_WIDTH-50, SCREEN_HEIGHT-90)
    
    SPACESHIP_SIZE = (90/1.5, 64/1.5)
    PLAYER1_IMG_LOADED = pygame.image.load(PLAYER1_IMG)
    PLAYER1_IMG_LOADED = pygame.transform.scale(PLAYER1_IMG_LOADED, SPACESHIP_SIZE).convert_alpha()
    
    PLAYER2_IMG_LOADED = pygame.image.load(PLAYER2_IMG)
    PLAYER2_IMG_LOADED = pygame.transform.scale(PLAYER2_IMG_LOADED, SPACESHIP_SIZE).convert_alpha()
    
    PLAYER1_THRUST = pygame.image.load(r"assets\ny_thrust.png").convert_alpha()
    PLAYER2_THRUST = pygame.image.load(r"assets\thrust_spaceship2.png")
    

    PLAYER2_THRUST = pygame.transform.scale(PLAYER2_THRUST, (SPACESHIP_SIZE)).convert_alpha()
    
    PLAYER_VELOCITY = 10
    ROTATION_SPEED = 0.1
    THRUST = 0.05
    
    # Laser beam
    PLAYER1_BEAM = "assets\player1_beam.png"
    PLAYER2_BEAM = "assets\player2_beam.png"
    
    BEAM_VELOCITY = 7
    MAX_BEAMS = 3
    
    
    # Platforms
    PLATFORM_IMG = "assets\platform.png"
    PLATFORM_SIZE = (81.9, 64)
    """ PLATFORM_PLAYER1_POSITION = (START_POSITION_PLAYER1[0]+30, START_POSITION_PLAYER1[1]+60)
    PLATFORM_PLAYER2_POSITION = (START_POSITION_PLAYER2[0]+30, START_POSITION_PLAYER2[1]+60) """
    
    PLATFORM_PLAYER1_POSITION = (START_POSITION_PLAYER1[0], START_POSITION_PLAYER1[1]+50)
    PLATFORM_PLAYER2_POSITION = (START_POSITION_PLAYER2[0], START_POSITION_PLAYER2[1]+50)
    
    # Obstacles
    OBSTACLE_IMG = "assets\obstacle.png"
    
    OBSTACLE_SIZE = (90, 90)
    
    OBSTACLE_POSITIONS = [(SCREEN_WIDTH-550, SCREEN_HEIGHT-250), (SCREEN_WIDTH-250, SCREEN_HEIGHT-150), (SCREEN_WIDTH-600, SCREEN_HEIGHT-100), (SCREEN_WIDTH-350, SCREEN_HEIGHT-400), (SCREEN_WIDTH-650, SCREEN_HEIGHT-500)]
    

    SCORE_PANEL = pygame.image.load("assets\score_panel.png")
    SCORE_PANEL = pygame.transform.scale(SCORE_PANEL, (820/4, 280/5)).convert_alpha()
    SCORE_PANEL_POS = (SCREEN_WIDTH/2-SCORE_PANEL.get_width()/2, 0)
    
    # Setting 
    GRAVITY = FPS/5000
    MAX_FUEL = 100
    FUEL_CONSUMPTION = 0.1
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
        self.velocity = Vec2(speed)
        self.position = Vec2(position)
        self.angle = np.degrees(0)
        
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
        
        self.shoot_cooldown = 0
        self.beams = pygame.sprite.Group()
        
        self.fuel = Config.MAX_FUEL
        self.score = Config.SCORE
        
        self.screen = Config.SCREEN
        
    def move(self):
        self.position += self.velocity
        self.velocity += Vec2(0, Config.GRAVITY)
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
        
    def thrust(self):
        if self.fuel > 0:
            thrust_vector = Vec2(0, Config.THRUST)
            thrust_vector.rotate_ip(-self.angle+180)
            self.velocity += thrust_vector
            self.fuel -= Config.FUEL_CONSUMPTION
        
    def move_right(self, image):
        self.angle -= np.degrees(Config.ROTATION_SPEED)
        rotate_image = pygame.transform.rotate(image, self.angle)
        rotate_rec = rotate_image.get_rect(center = self.rect.center)
        return rotate_image, rotate_rec
    
    def move_left(self, image):
        self.angle += np.degrees(Config.ROTATION_SPEED)
        rotate_image = pygame.transform.rotate(image, self.angle)
        rotate_rec = rotate_image.get_rect(center = self.rect.center)
        return rotate_image, rotate_rec
    
    def boundaries(self):
        if self.position.x < 0:
            self.velocity.x = -self.velocity.x
        elif self.position.x > Config.SCREEN_WIDTH:
            self.velocity.x = -self.velocity.x
        if self.position.y < 0:
            self.velocity.y = -self.velocity.y
        elif self.position.y > Config.SCREEN_HEIGHT:
            self.velocity.y = -self.velocity.y
        
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        self.move()
        self.draw()
        self.boundaries()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def reset(self):
        self.position = Vec2(self.start_pos)
        self.velocity = Vec2(0, 0)
        self.fuel = Config.MAX_FUEL
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
        self.rect.center = self.position
        
        
        
        
""" _______LASER_BEAM_______ """

class LaserBeam(pygame.sprite.Sprite):
    def __init__(self, image, position, angle):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (20, 20)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = Config.BEAM_VELOCITY
    
        self.position = Vec2(position)
        self.speed = Vec2(0, 0)
        self.angle = angle
        
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
        
        self.screen = Config.SCREEN
        
    def draw(self):
        self.screen.blit(self.image, self.rect) 
    
    # Move the beam in the direction of the spaceship 
    def move(self):
        self.position += Vec2(self.velocity, 0).rotate(-self.angle-90)
        self.rect = self.image.get_rect(center = (self.position.x, self.position.y))
        
    def update(self):
        self.move()
        self.draw()
       
        
        
""" _______PLATFORMS_______ """

class Platforms(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(Config.PLATFORM_IMG)
        self.image = pygame.transform.scale(self.image, Config.PLATFORM_SIZE).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.screen = Config.SCREEN
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        self.draw()
        
        
""" _______OBSTACLES_______ """
class Obstacles(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, Config.OBSTACLE_SIZE).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        
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
        self.player1_spaceship = Spaceships(Config.PLAYER1_IMG, Config.START_POSITION_PLAYER1, (0,0))
        self.player2_spaceship = Spaceships(Config.PLAYER2_IMG, Config.START_POSITION_PLAYER2, (0,0))
        self.spaceship_group = pygame.sprite.Group()
        for spaceship in self.player1_spaceship, self.player2_spaceship:
            self.spaceship_group.add(spaceship)
        
        # Platforms
        self.player1_platform = Platforms(Config.PLATFORM_PLAYER1_POSITION[0], Config.PLATFORM_PLAYER1_POSITION[1])
        self.player2_platform = Platforms(Config.PLATFORM_PLAYER2_POSITION[0], Config.PLATFORM_PLAYER2_POSITION[1])
        self.platform_group = pygame.sprite.Group()
        for platform in self.player1_platform, self.player2_platform:
            self.platform_group.add(platform)
            
        # Obstacles
        self.obstacle_group = pygame.sprite.Group()
        for positions in range(len(Config.OBSTACLE_POSITIONS)):
            obstacle = Obstacles(Config.OBSTACLE_IMG, Config.OBSTACLE_POSITIONS[positions])
            self.obstacle_group.add(obstacle)
        
        # Player 1 controls
    def event_handler(self):
        keys = pygame.key.get_pressed()
        
        # Player 1 controls
        if keys[pygame.K_w] and self.player1_spaceship.rect.y > 0:
            self.player1_spaceship.image = pygame.transform.rotate(Config.PLAYER1_THRUST, self.player1_spaceship.angle)
            self.player1_spaceship.thrust()
        if keys[pygame.K_d] and self.player1_spaceship.rect.x < Config.SCREEN_WIDTH - self.player1_spaceship.image_width:
            self.player1_spaceship.image, self.player1_spaceship.rect = self.player1_spaceship.move_right(Config.PLAYER1_IMG_LOADED)
        if keys[pygame.K_a] and self.player1_spaceship.rect.x > 0:
            self.player1_spaceship.image, self.player1_spaceship.rect = self.player1_spaceship.move_left(Config.PLAYER1_IMG_LOADED)
        if keys[pygame.K_w] == False:
            self.player1_spaceship.image = pygame.transform.rotate(Config.PLAYER1_IMG_LOADED, self.player1_spaceship.angle)
        
        # Player 2 controls
        if keys[pygame.K_UP] and self.player2_spaceship.rect.y > 0:
            self.player2_spaceship.thrust()
        if keys[pygame.K_RIGHT] and self.player2_spaceship.rect.x < Config.SCREEN_WIDTH - self.player2_spaceship.image_width:
            self.player2_spaceship.image, self.player2_spaceship.rect = self.player2_spaceship.move_right(Config.PLAYER2_IMG_LOADED)
        if keys[pygame.K_LEFT] and self.player2_spaceship.rect.x > 0:
            self.player2_spaceship.image, self.player2_spaceship.rect = self.player2_spaceship.move_left(Config.PLAYER2_IMG_LOADED)
        if keys[pygame.K_UP] == False:
            self.player2_spaceship.image = pygame.transform.rotate(Config.PLAYER2_IMG_LOADED, self.player2_spaceship.angle)
        
        # Shoot
    def shootkeys(self, spaceship):
        keys = pygame.key.get_pressed()
        if spaceship == self.player1_spaceship:
            if keys[pygame.K_LCTRL]:
                if self.player1_spaceship.shoot_cooldown == 0:
                    self.player1_spaceship.shoot_cooldown = 20
                    spaceship.beams.add(LaserBeam(Config.PLAYER1_BEAM, (spaceship.rect.centerx, spaceship.rect.centery), self.player1_spaceship.angle))
        elif spaceship == self.player2_spaceship:
            if keys[pygame.K_RCTRL]:
                if self.player2_spaceship.shoot_cooldown == 0:
                    self.player2_spaceship.shoot_cooldown = 20
                    spaceship.beams.add(LaserBeam(Config.PLAYER2_BEAM, (spaceship.rect.centerx, spaceship.rect.centery), self.player2_spaceship.angle))

    def hit_by_beam(self):
        if pygame.sprite.spritecollide(self.player1_spaceship, self.player2_spaceship.beams, True):
            self.player1_spaceship.reset()
            self.player2_spaceship.score += 1
        if pygame.sprite.spritecollide(self.player2_spaceship, self.player1_spaceship.beams, True):
            self.player2_spaceship.reset()
            self.player1_spaceship.score += 1
    
    def collison_between_spaceships(self):
        if pygame.sprite.collide_mask(self.player1_spaceship, self.player2_spaceship):
            self.player1_spaceship.reset() 
            self.player2_spaceship.reset()
            
            self.player1_spaceship.score -= 1
            self.player2_spaceship.score -= 1
            
    def collision_platform(self):
        for platform in self.platform_group:
            if pygame.sprite.collide_rect(self.player1_spaceship, platform) and self.player1_spaceship.velocity.y > 0:
                self.player1_spaceship.velocity.y = 0
                self.player1_spaceship.rect.top= platform.rect.bottom
                self.player1_spaceship.fuel = Config.MAX_FUEL
            if pygame.sprite.collide_rect(self.player2_spaceship, platform) and self.player2_spaceship.velocity.y > 0:
                self.player2_spaceship.velocity.y = 0
                self.player2_spaceship.rect.bottom = platform.rect.top
                self.player2_spaceship.fuel = Config.MAX_FUEL
               
        
    def collision_obstacles(self):
        for obstacle in self.obstacle_group:
            if pygame.sprite.collide_mask(self.player1_spaceship, obstacle):
                print("collision")
                self.player1_spaceship.reset()
                self.player1_spaceship.score -= 1
            if pygame.sprite.collide_mask(self.player2_spaceship, obstacle):
                self.player2_spaceship.reset()
                self.player2_spaceship.score -= 1
        # laserbeam collision with obstacles -> destroy laserbeam (dokill = False, dokill2 = True)
        if pygame.sprite.groupcollide(self.obstacle_group, self.player1_spaceship.beams, False, True):
            pass
        if pygame.sprite.groupcollide(self.obstacle_group, self.player2_spaceship.beams, False, True):
            pass
        
    def score(self):
        Config.SCREEN.blit(Config.SCORE_PANEL, Config.SCORE_PANEL_POS)
        Config.SCREEN.blit(Config.SCORE_FONT.render(str(self.player1_spaceship.score), True, (255,255,255)), (Config.SCREEN_WIDTH/2-60, 10))
        Config.SCREEN.blit(Config.SCORE_FONT.render(str(self.player2_spaceship.score), True, (255,255,255)), (Config.SCREEN_WIDTH/2+50, 10))
        
        
    def fuel_bar(self):    
        pygame.draw.rect(Config.SCREEN, (47,150,39,255), (0, Config.SCREEN_HEIGHT-10, self.player1_spaceship.fuel, 10))
        pygame.draw.rect(Config.SCREEN, (148,85,194,255), (Config.SCREEN_WIDTH-self.player2_spaceship.fuel, Config.SCREEN_HEIGHT-10, self.player2_spaceship.fuel, 10))
        
        
    def collision(self):
        self.collision_platform()
        self.collision_obstacles()
        self.collison_between_spaceships()
        self.hit_by_beam()
        
   
    def update(self):
        self.spaceship_group.update()
        self.platform_group.update()
        self.obstacle_group.update()
        self.player1_spaceship.beams.update()
        self.player2_spaceship.beams.update()
        
        
    def draw(self):
        Config.SCREEN.blit(Config.BACKGROUND, (0, 0))
        
        self.player1_spaceship.beams.draw(Config.SCREEN)
        self.player2_spaceship.beams.draw(Config.SCREEN)
        self.spaceship_group.draw(Config.SCREEN)
        self.platform_group.draw(Config.SCREEN)
        self.obstacle_group.draw(Config.SCREEN)  
        self.fuel_bar()  
        self.score()
        
        pygame.display.update()
        
        
    def game_loop(self):
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

            self.clock.tick(Config.FPS)
            
            
            self.event_handler()
            self.shootkeys(self.player1_spaceship)
            self.shootkeys(self.player2_spaceship)
            self.collision()
            self.update()
            self.draw()
            
            
            pygame.display.update()



if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.game_loop()
