import pygame as pg
import random
import time

SCREEN_X = 800
SCREEN_Y = 600
BG_FILE = "sushiplate.jpg"
BALL_FILE = "ball.png"
FUGU_FILE = "fugu.png"

pg.init()

screen = pg.display.set_mode((SCREEN_X, SCREEN_Y), 0)
background = pg.image.load(BG_FILE)
background = pg.transform.scale(background, (SCREEN_X, SCREEN_Y))
background.convert()

fugu = pg.image.load(FUGU_FILE)
ball = pg.image.load(BALL_FILE)

# Klasse som inneholder x pos og y pos, samt bilde
class Drawable:
    
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        
    def move(self): # bruker den i draw
        pass
        
    def draw(self):
        self.move() 
        screen.blit(self.img, (self.x,self.y))
 # subklasse av Drawable som har en speed variabel

class Fish(Drawable):
    
    def __init__(self, x, y, img, speed):
        super().__init__(x, y, img) 
        self.speed = speed
    # flytter fiskene
    def move(self):
        self.x = self.x + self.speed
        if self.x < 0:
            self.speed = abs(self.speed)
        if self.x > SCREEN_X:
            self.speed = -abs(self.speed)
            
class Ball(Drawable):
     # subklasse av Drawable som har en speed variabel i x og y retning
    def __init__(self, x, y, speed):
        super().__init__(x, y, ball)
        self.speed_x = speed[0]
        self.speed_y = speed[1]
    # flytter ballene kræsjer de med veggen i x eller y retning
    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        if self.x < 0:
            self.speed_x = abs(self.speed_x)
        if self.y < 0:
            self.speed_y = abs(self.speed_y)
        if self.x > SCREEN_X:
            self.speed_x = -abs(self.speed_x)
        if self.y > SCREEN_Y:
            self.speed_y = -abs(self.speed_y)

# lager en liste med 10 baller og 3 fisker 
my_balls = []
for _ in range(10):
    x_pos = random.randint(0, SCREEN_X)
    y_pos = random.randint(0, SCREEN_Y)
    x_speed = random.randint(1, 4)
    y_speed = random.randint(1,4)
    my_balls.append(Ball(x_pos, y_pos, (x_speed, y_speed)))

fish = []
for _ in range(3):
    x_pos = random.randint(0, SCREEN_X)
    y_pos = random.randint(0, SCREEN_Y)
    speed = random.randint(1, 2)
    fish.append(Fish(x_pos, y_pos, fugu ,speed))


prev_time = time.time() * 1000
while True:
    now = time.time() * 1000
    if now - prev_time > 10: # 100 fps
        event = pg.event.poll()
        if event.type == pg.QUIT: # avslutter programmet med krysset på vinduet
            break
        
        screen.blit(background, (0,0)) # første vi vil gjøre
        for ball in my_balls:
            ball.draw() # tegner ballene
        for my_fish in fish:
            my_fish.draw() # tegner fiskene
        pg.display.update() # oppdaterer skjermen
        prev_time = now  # oppdaterer tiden
print("Goodbye...")