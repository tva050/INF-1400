import pygame as pg
import random
import time

SCREEN_X = 800
SCREEN_Y = 600
BOIDS_FILE = "Mandetory 2\Figures\Boids.png"
HOIKS_FILE = "Mandetory 2\Figures\predator.png"
OBSTICALS_FILE = "Mandetory 2\Figures\obstical.png"
BG_FILE = "Mandetory 2\Figures\sky_bg.png"

pg.init()

screen = pg.display.set_mode((SCREEN_X, SCREEN_Y), 0)
background = pg.image.load(BG_FILE)
background = pg.transform.scale(background, (SCREEN_X, SCREEN_Y)).convert()


boids = pg.image.load(BOIDS_FILE)
hoiks = pg.image.load(HOIKS_FILE)
obstacles = pg.image.load(OBSTICALS_FILE)


# Class for all objects that can be drawn on the screen
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

class moves(Drawable):
    
    def __init__(self, x, y, img, speed):
        super().__init__(x, y, img)
        self.speed = speed


# Class for Boids which is a subclass of Drawable and has a speed variable
class Boids(Drawable):
    
    def __init__(self, x, y, speed):
        super().__init__(x, y, boids)
        self.speed = speed
    
    def separation(self): # Moves boids away from each other if they are too close to each other (don't crash!)
        pass
    
    def alignment(self): # Moves boids in the same direction and speed as the other boids in the flock
        pass
    
    def cohesion(self): # Moves boids towards the center of the flock
        pass
    
    def avoid_hoiks(self):
        pass
    
    def avoid_obstacles(self):
        pass
    

class Hoiks(Drawable):
    # Hoiks dont need to move in a flock, they just move in random directions, but
    # if they crash into a boid they eat it.
    def __init__(self, x, y, speed):
        super().__init__(x, y, hoiks)
        self.speed = speed
    
class Obstacles(Drawable):
    # Obstacles are just static objects that the boids and hoiks can't pass through
    def __init__(self, x, y, img):
        super().__init__(x, y, img)
    
    def boundaries(self):
        pass
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))  



while True:
    
    event = pg.event.wait()
    if event.type == pg.QUIT: # avslutter programmet med krysset på vinduet
        break
    
    screen.blit(background, (0,0)) # første vi vil gjøre
    Obstacles(0, 0, obstacles).draw()
    pg.display.update() # oppdaterer skjermen
    
print("GOODBYE, for now!")

