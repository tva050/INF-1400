import pygame 

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


""" _______SPACESHIPS_______ """
class Spaceships(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, Config.SPACESHIP_SIZE).convert_alpha()
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        
        self.x_velocity = 0
        self.y_velocity = 0
        self.velocity = 0
        
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        
        self.screen = Config.SCREEN
        self.gravity = Config.GRAVITY
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    def spaceship_boundaries(self):
        if self.rect.x > Config.SCREEN_WIDTH:
            self.x_velocity = -1 
        elif self.rect.x < 0:
            self.x_velocity = 1
        elif self.rect.y > Config.SCREEN_HEIGHT:
            self.y_velocity = -1
        elif self.rect.y < 0:   
            self.y_velocity = 1
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def thrust(self): # motion upwards of the spaceship
        self.y_velocity = -self.velocity
    
    def move_right(self): 
        self.x_velocity = self.velocity
    
    def move_left(self):
        self.x_velocity = -self.velocity
    
    def update(self):
        self.move(self.x_velocity, self.y_velocity)
        self.spaceship_boundaries()
        
        self.y_velocity += self.gravity
        self.x_velocity = 0
        
        self.draw()

""" _______PLATFORMS_______ """



""" _______OBSTACLES_______ """




""" _______GAME_______ """

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        
        # Spaceships
        self.player1_spaceship = Spaceships(Config.PLAYER1_IMG, Config.START_POSITION_PLAYER1)
        self.spaceship_group = pygame.sprite.Group()
        self.spaceship_group.add(self.player1_spaceship)
    
    def draw(self):
        Config.SCREEN.blit(Config.BACKGROUND, (0, 0))
        self.player1_spaceship.draw()
        
        pygame.display.update()
        
    def event_handler(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.player1_spaceship.thrust()
        if keys[pygame.K_RIGHT]:
            self.player1_spaceship.move_right()
        if keys[pygame.K_LEFT]:
            self.player1_spaceship.move_left()
    
    def update(self):
        self.player1_spaceship.update()

        
    
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



if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.game_loop()

        
        
        