import pygame

X_SIZE = 800
Y_SIZE = 600
BG_file = "sushiplate.jpg"
BALL_FILE = "fugu.png"


pygame.init()

screen = pygame.display.set_mode((X_SIZE, Y_SIZE), 0)
background = pygame.image.load(BG_file)
background = pygame.transform.scale(background, (X_SIZE, Y_SIZE))
background.convert()

ball = pygame.image.load(BALL_FILE)
ball_center = ball.get_width() / 2
ball_center = ball.get_height() / 2


while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
    
    screen.blit(background, (0, 0))
    if event.type == pygame.MOUSEMOTION:
        ball_center_x = pygame.mouse.get_pos()[0] - ball.get_width() / 2
        ball_center_y = pygame.mouse.get_pos()[1] - ball.get_height() / 2
        
        screen.blit(ball, (ball_center_x, ball_center_y))
    pygame.display.update()
    
print("Finished exection")
    
