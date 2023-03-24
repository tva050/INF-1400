import pygame

from config import Config
from spaceships import Spaceships
from laserbeam import LaserBeam
from platforms import Platforms
from obstacles import Obstacles


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
        

       
    def multiple_shoot(self, spaceship):
        if spaceship == self.player1_spaceship:
            if self.player1_spaceship.shoot_cooldown == 0:
                self.player1_spaceship.shoot_cooldown = 20
                player1_laser_beam = LaserBeam(Config.PLAYER1_BEAM, (spaceship.rect.centerx, spaceship.rect.top))
                self.spaceship_group.add(player1_laser_beam)
        elif spaceship == self.player2_spaceship:    
            if self.player2_spaceship.shoot_cooldown == 0:
                self.player2_spaceship.shoot_cooldown = 20
                player2_laser_beam = LaserBeam(Config.PLAYER2_BEAM, (spaceship.rect.centerx, spaceship.rect.top))
                self.spaceship_group.add(player2_laser_beam)
        
        
        
        
    def draw(self):
        Config.SCREEN.blit(Config.BACKGROUND, (0, 0))
        
        self.spaceship_group.draw(Config.SCREEN)
        self.platform_group.draw(Config.SCREEN)
        self.obstacle_group.draw(Config.SCREEN)
    
        pygame.display.update()
    
        
    def event_handler(self):
        keys = pygame.key.get_pressed()
        
        # Player 1 controls
        if keys[pygame.K_w] and self.player1_spaceship.rect.y > 0:
            self.player1_spaceship.thrust(Config.PLAYER_VELOCITY)
        if keys[pygame.K_d] and self.player1_spaceship.rect.x < Config.SCREEN_WIDTH - self.player1_spaceship.image_width:
            self.player1_spaceship.move_right(Config.PLAYER_VELOCITY)
        if keys[pygame.K_a] and self.player1_spaceship.rect.x > 0:
            self.player1_spaceship.move_left(Config.PLAYER_VELOCITY)
        
        # Player 2 controls
        if keys[pygame.K_UP] and self.player2_spaceship.rect.y > 0:
            self.player2_spaceship.thrust(Config.PLAYER_VELOCITY)
        if keys[pygame.K_RIGHT] and self.player2_spaceship.rect.x < Config.SCREEN_WIDTH - self.player2_spaceship.image_width:
            self.player2_spaceship.move_right(Config.PLAYER_VELOCITY)
        if keys[pygame.K_LEFT] and self.player2_spaceship.rect.x > 0:
            self.player2_spaceship.move_left(Config.PLAYER_VELOCITY)
        
        # Shoot
        
        if keys[pygame.K_LCTRL]: #and not self.player1_spaceship.fired_beam_state:
            self.multiple_shoot(self.player1_spaceship)
        if keys[pygame.K_RCTRL]: #and not self.player2_spaceship.fired_beam_state:
            self.multiple_shoot(self.player2_spaceship)
           
        
            
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        break

            self.clock.tick(Config.FPS)
            
            self.event_handler()
            self.collision()
            self.update()
            self.draw()
            
            
            pygame.display.update()

        
    

        
    