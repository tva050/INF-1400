import pygame, sys


pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Shadow of the Moon")
# Screen size
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
# Screen size
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
# Background image
BACKGROUND = pygame.image.load("assets\space_background.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() 
PLAYER1_IMG = "assets\player1.png" 
PLAYER2_IMG = "assets\player2.png"
# Obstacle and platform images
PLATFORM = "assets\startpad.png"
PLATFORM_PLAYER1_POS = (100, 200)
PLATFORM_PLAYER2_POS = (600, 700)


class Spaceships(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__() 
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (71.9, 54))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def draw(self): 
        SCREEN.blit(self.image, self.rect)
        
class Platform(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        
    def draw(self):
        SCREEN.blit(self.image, self.rect)
        

spaceship_player1 = Spaceships(PLAYER1_IMG, 100, 100)
spaceship_player2 = Spaceships(PLAYER2_IMG, 600, 700)

spaceship_group = pygame.sprite.Group()
for spaceship in spaceship_player1, spaceship_player2:
    spaceship_group.add(spaceship)
    
platform_1 = Platform(PLATFORM, PLATFORM_PLAYER1_POS[0], PLATFORM_PLAYER1_POS[1])
platform_2 = Platform(PLATFORM, PLATFORM_PLAYER2_POS[0], PLATFORM_PLAYER2_POS[1])

platform_group = pygame.sprite.Group()
for platform in platform_1, platform_2:
    platform_group.add(platform)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    SCREEN.blit(BACKGROUND, (0, 0))
    spaceship_group.draw(SCREEN)
    platform_group.draw(SCREEN)
    
    pygame.display.flip()
    clock.tick(60)


    
