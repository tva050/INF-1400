import pygame 



""" _______CONFIG_______ """

class Config:

    pygame.display.set_caption("Mayhem")
    
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    FPS = 60 # Frames per second
    
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
    
    BACKGROUND = pygame.image.load("assets\space_background.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() 
    
    PLAYER1_IMG = "assets\spaceship1.png"
    
    PLAYER1_POSITION = (SCREEN_WIDTH-840, SCREEN_HEIGHT-50)
    PLAYER1_VELOCITY = 30
    
    GRAVITY = 10

class Player(pygame.sprite.Sprite):
    def __init__(self, image, position, id):
        super().__init__()
        
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (90/1.5, 64/1.5)).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x_vel = 0
        self.y_vel = 0
    
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.rect.center = [self.rect.x, self.rect.y]

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        
    def move_left(self, vel):
        self.x_vel = -vel
    def move_right(self, vel):
        self.x_vel = vel
    
    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
class Game:
    def __init__(self):
        

    
