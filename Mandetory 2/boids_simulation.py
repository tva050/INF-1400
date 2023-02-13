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
class Moving:
    
    def __init__(self):
        self.position = Vec2(random.randint(20, 800), random.randint(20, 600))
        self.velocity = Vec2(random.uniform(-1, 1), random.uniform(-1, 1))
        
        self.perceived_distance = 100

        
    def move(self):
        self.position = self.position + self.velocity
        if self.position.x < 0:
            self.velocity.x = abs(self.velocity.x)
        if self.position.y < 0:
            self.velocity.y = abs(self.velocity.y)
        if self.position.x > SCREEN_X:
            self.velocity.x = -abs(self.velocity.x)
        if self.position.y > SCREEN_Y:
            self.velocity.y = -abs(self.velocity.y)
    
    def update(self):
        self.position += self.velocity
        
    
    #def separtion(self):
    """ The separation function, is used to make the boids """    
    
    def alginment(self, boids):
        """ 
        Every boid sees the locoal boids, so the boids will try to algin with the other boids. Doing this by
        taking the average of the velocity of the boids in the local area. 
        """
        local_boids = [] # List of boids in the local area
        for boid in boids: 
            if boid.position.distance_to(self.position) < self.perceived_distance: # if the boid is in the local area at a distance of 100
                local_boids.append(boid)
        if len(local_boids) > 0: # if there are boids in the local area
            avg_vel = Vec2(0, 0) # average velocity
            for boid in local_boids: # for every boid in the local area
                avg_vel += boid.velocity # average velocity is added to the velocity of the boid
            avg_vel /= len(local_boids) # 
            self.velocity = (self.velocity + avg_vel) / 2  
            self.velocity.scale_to_length(2) 
          
    def cohesion(self, boids):
        """ 
        The cohesion function, is used to make the boids try to stay together, by making the boids try to go to the center of the local boids
        """
        local_boids = []
        for boid in boids:
            if boid.position.distance_to(self.position) < self.perceived_distance:
                local_boids.append(boid)
        if len(local_boids) > 0:
            avg_pos = Vec2(0, 0)
            for boid in local_boids:
                avg_pos +=
                    
            


""" 
---- Trying to make a class that can draw objects ----
class Drawable:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
    
    def draw(self, objects):
        self.move()
        screen.blit(self.img, (self.x, self.y))
        for obj in objects:
            obj.draw() """

class Boids(Moving): # In class Boids we will use the class Moves to move, for us the be availble to move something we need to first draw it
    
    def __init__(self):
        super().__init__()
    
    def draw(self):
        self.move()
        self.update()
        self.alginment(boids) # This is the alginment function
        screen.blit(boid, (self.position.x, self.position.y))
    
    
    

#class Hoiks(Moves):

#class Objects(MOves):

def draw():
    for boid in boids:
        boid.draw()

boids = [Boids() for _ in range(20)]


prev_time = time.time() * 1000
while True:
    now = time.time() * 1000
    if now - prev_time > 60:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            break
        
        screen.blit(background, (0,0))
        draw()
        
        pg.display.update()
        prev_time = now
print("Good bye, for now! ")
        