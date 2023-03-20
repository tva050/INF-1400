import pygame 

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)

BACKGROUND = pygame.image.load("assets\space_background.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert() 
    
PLAYER1_IMG = pygame.image.load("assets\spaceship1.png")
PLAYER1_IMG = pygame.transform.scale(PLAYER1_IMG, (90/1.5, 64/1.5)).convert_alpha()


x, y = 900/2, 600/2

while True:
    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(PLAYER1_IMG, (x, y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]: 
        x += 2
    if pressed[pygame.K_LEFT]:
        x -= 2
    if pressed[pygame.K_UP]:
        y -= 2
    if pressed[pygame.K_DOWN]:
        y += 2
    pygame.display.update()
    
    clock.tick(60)


    
