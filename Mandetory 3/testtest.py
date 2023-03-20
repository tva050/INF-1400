import pygame 
from pygame import Vector2 as Vec2

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
GRAVITY = Vec2(10, 10)


class Player1(pygame.sprite.Sprite):
    def __init__(self, position, speed):
        super().__init__()
        self.image = pygame.image.load("assets\spaceship1.png")
        self.image = pygame.transform.scale(self.image, (90/1.5, 64/1.5)).convert_alpha()

        self.clock = pygame.time.Clock()
        self.time = self.clock.tick(30) / 1000.0
        
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.rect.center = [self.rect.x, self.rect.y]
        
        self.speed = Vec2(-1, -1)
        self.thrust = Vec2(0, -3)
        
        self.acceleration = self.thrust + GRAVITY
        
        self.new_speed = self.speed + self.acceleration * self.time
        self.max_speed = Vec2(-2, -2)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            self.rect.x += self.new_speed.x
            self.rect.y += self.new_speed.y
            #self.rect.center = [self.rect.x, self.rect.y]
        if pressed[pygame.K_DOWN]:
            self.rect.y += GRAVITY.y
        
    
class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        
        self.player1_spaceship = Player1((x, y), (0, 0))
        self.player1_spaceship_group = pygame.sprite.Group()
        self.player1_spaceship_group.add(self.player1_spaceship)
    
    
    def player1(self):
        
    
    def run(self):
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
            
            SCREEN.blit(BACKGROUND, (0, 0))
            
        
            self.player1_spaceship_group.update()
            self.player1_spaceship_group.draw(SCREEN)
            
            
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()

    
