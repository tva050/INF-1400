import pygame

from config import Config
from spaceships import Spaceships
from laserbeam import LaserBeam
from platforms import Platforms
from obstacles import Obstacles


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
        
    def fuel_bar(self):    
        pygame.draw.rect(Config.SCREEN, (47,150,39,255), (0, Config.SCREEN_HEIGHT-10, self.player1_spaceship.fuel, 10))
        pygame.draw.rect(Config.SCREEN, (148,85,194,255), (Config.SCREEN_WIDTH-self.player2_spaceship.fuel, Config.SCREEN_HEIGHT-10, self.player2_spaceship.fuel, 10))
        
    def score(self):
        Config.SCREEN.blit(Config.SCORE_PANEL, Config.SCORE_PANEL_POS)
        Config.SCREEN.blit(Config.FONT.render(str(self.player1_spaceship.score), True, (255,255,255)), (Config.SCREEN_WIDTH/2-60, 10))
        Config.SCREEN.blit(Config.FONT.render(str(self.player2_spaceship.score), True, (255,255,255)), (Config.SCREEN_WIDTH/2+50, 10))
        
    def draw_winner(self):
        if self.player1_spaceship.score == 1:
            Config.SCREEN.blit(Config.GREEN_WON, (Config.WON_PANEL_POS))
        elif self.player2_spaceship.score == 1:
            Config.SCREEN.blit(Config.PURPLE_WON, (Config.WON_PANEL_POS))
        # draw a black transparent rectangle behind the winner text
        pygame.display.update()
        pygame.time.delay(10_000)
        
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
                    
            if self.player1_spaceship.score == 1 or self.player2_spaceship.score == 1:
                self.draw_winner()
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
