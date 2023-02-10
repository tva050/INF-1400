import pygame as pg
import random
import time

SCREEN_X = 800
SCREEN_Y = 600
BOIDS_FILE = "Mandetory 2\Figures\Boids.png"
HOIKS_FILE = "Mandetory 2\Figures\Predator.png"
BG_FILE = "Mandetory 2\Figures\mabynow.png"

pg.init()

screen = pg.display.set_mode((SCREEN_X, SCREEN_Y), 0)
background = pg.image.load(BG_FILE)
background = pg.transform.scale(background, (SCREEN_X, SCREEN_Y)).convert()


boids = pg.image.load(BOIDS_FILE)
hoiks = pg.image.load(HOIKS_FILE)

#

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

class Boids(Drawable):
    
    def __init__(self, x, y, speed):
        super().__init__(x, y, boids)
        self.speed = speed

class Hoiks(Drawable):
    
    def __init__(self, x, y, speed):
        super().__init__(x, y, hoiks)
        self.speed = speed

class Obstacles(Drawable):
    
    def __init__(self, x, y, img):
        super().__init__(x, y, img)  

while True:
    
    event = pg.event.wait()
    if event.type == pg.QUIT: # avslutter programmet med krysset på vinduet
        break
    
    screen.blit(background, (0,0)) # første vi vil gjøre
    
    pg.display.update() # oppdaterer skjermen
    
print("GOODBYE, for now!")

