import pygame 
""" 
class Config:
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    FPS = 60


    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)

    BACKGROUND = pygame.image.load("assets\space_background.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() 

    PLAYER1_IMG = pygame.image.load("assets\spaceship1.png")
    PLAYER1_IMG = pygame.transform.scale(PLAYER1_IMG, (90/1.5, 64/1.5)).convert_alpha()

    x, y = 900/2, 600/2
    PLAYER_VEL = 5
    GRAVITY = 10

class player(pygame.sprite.Sprite):
    def __init__(self, position, speed):
        super().__init__()
        self.image = pygame.image.load("assets\spaceship1.png")
        self.image = pygame.transform.scale(self.image, (90/1.5, 64/1.5)).convert_alpha()

        self.x_vel = 0
        self.y_vel = 0
        self.direction = "left"
        
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.rect.center = [self.rect.x, self.rect.y]
        
        self.fall_count = 0
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            
    
    def move_rigth(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
    
    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * Config.GRAVITY)
        self.move(self.x_vel, self.y_vel)
        
        self.fall_count += 1
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
        
def handle_move(player):
    keys = pygame.key.get_pressed()
    
    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(Config.PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_rigth(Config.PLAYER_VEL)
    if keys[pygame.K_UP]:
        player.y_vel = -Config.PLAYER_VEL
        player.fall_count = 0
    
         

player = player((Config.x, Config.y), (0, 0))
        
def game_loop():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(Config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        Config.SCREEN.blit(Config.BACKGROUND, (0, 0))
        player.loop(Config.FPS) 
        handle_move(player)
        player.draw(Config.SCREEN)
      
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    game_loop()
     """
    
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
    START_POSITION_PLAYER1 = (SCREEN_WIDTH-840, SCREEN_HEIGHT-95)
    START_POSITION_PLAYER2 = (SCREEN_WIDTH-60, SCREEN_HEIGHT-95)
    
    SPACESHIP_SIZE = (90/1.5, 64/1.5)
    PLAYER_VELOCITY = 5
    
    # Platforms
    PLATFORM_IMG = "assets\platform.png"
    
    PLATFORM_PLAYER1_POSITION = (SCREEN_WIDTH-840, SCREEN_HEIGHT-50)
    PLATFORM_PLAYER2_POSITION = (SCREEN_WIDTH-60, SCREEN_HEIGHT-50)
    
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

class Spaceships(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, Config.SPACESHIP_SIZE).convert_alpha()
        
        self.screen = Config.SCREEN
        
        
        