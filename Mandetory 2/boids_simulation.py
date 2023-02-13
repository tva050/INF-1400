""" 
import pygame as pg
import random
import time

SCREEN_X = 800
SCREEN_Y = 600
#BOIDS_FILE = r"Mandetory 2\Figures\fugu.png"
BOID_FILE = "Mandetory 2\Figures\Boids.png"
HOIK_FILE = "Mandetory 2\Figures\predator.png"
OBSTICALS_FILE = "Mandetory 2\Figures\obstical.png"
BG_FILE = "Mandetory 2\Figures\sky_bg.png"

pg.init()

screen = pg.display.set_mode((SCREEN_X, SCREEN_Y), 0)
background = pg.image.load(BG_FILE)
background = pg.transform.scale(background, (SCREEN_X, SCREEN_Y))
background.convert()

boid = pg.image.load(BOID_FILE)
boid = pg.transform.scale(boid, (10, 10))
hoik = pg.image.load(HOIK_FILE)
hoik = pg.transform.scale(hoik, (10, 10))
obstical = pg.image.load(OBSTICALS_FILE)
obstical = pg.transform.scale(obstical, (15, 15))

class Drawable:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
    
    def move(self):
        pass
    
    def draw(self):
        self.move()
        screen.blit(self.img, (self.x, self.y))

class Boid(Drawable):
    def __init__(self, x, y, speed):
        super().__init__(x,y, boid)
        self.speed_x = speed[0]
        self.speed_y = speed[1]
        
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
            
    def update(self):
        self.x += self.

single_boid = Boid(SCREEN_X/2, SCREEN_Y/2, (2,2))

while True:
    event = pg.event.poll()
    if event.type == pg.QUIT:
        break
    
    screen.blit(background, (0,0))
    single_boid.draw()
    
    pg.display.update() # oppdaterer skjermen """

import pygame as pg
from pygame import Vector2 as Vec2
import random
import time

SCREEN_X = 800
SCREEN_Y = 600
#BOIDS_FILE = r"Mandetory 2\Figures\fugu.png"
BOID_FILE = "Mandetory 2\Figures\Boids.png"
HOIK_FILE = "Mandetory 2\Figures\predator.png"
OBSTICALS_FILE = "Mandetory 2\Figures\obstical.png"
BG_FILE = "Mandetory 2\Figures\sky_bg.png"

pg.init()

screen = pg.display.set_mode((SCREEN_X, SCREEN_Y), 0)
background = pg.image.load(BG_FILE)
background = pg.transform.scale(background, (SCREEN_X, SCREEN_Y)).convert()

boid = pg.image.load(BOID_FILE)
boid = pg.transform.scale(boid, (10, 10))
hoik = pg.image.load(HOIK_FILE)
hoik = pg.transform.scale(hoik, (10, 10))
obstical = pg.image.load(OBSTICALS_FILE)
obstical = pg.transform.scale(obstical, (15, 15))

# Class Moves which makes the possition, speed
class Moves:
    
    def __init__(self):
        self.position = Vec2(random.randint(800), random.randint(600))
        self.velocity = Vec2(random.randint(0.5, 1.5), random.randint(0.5, 1.5))
        
    def edges(self):
        self.position = self.position + self.velocity
        if self.position.x < 0:
            self.velocity.x = abs(self.velocity.x)
        if self.position.y < 0:
            self.velocity.x = abs(self.velocity.y)
        
    
    #def separtion(self, x, y):
    
    #def alginment(x,y,z):
    
    #def cohesion:
    

#class Boids(Moves): # In class Boids we will use the class Moves to move, for us the be availble to move something we need to first draw it

#class Hoiks(Moves):

#class Objects(MOves):

