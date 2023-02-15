import pygame as pg
from pygame import Vector2 as Vec2
import math
import random
import time

SCREEN_X = 800
SCREEN_Y = 600
#BOID_FILE = r"Mandetory 2\Figures\right-arrow.png"
BOID_FILE = r"Mandetory 2\Figures\navigate.png"
HOIK_FILE = r"Mandetory 2\Figures\hoik.png"
OBSTICALS_FILE = r"Mandetory 2\Figures\obstical.png"
#BG_FILE = "Mandetory 2\Figures\sky_bg.png"
#BG_FILE = r"Mandetory 2\Figures\bk.jpg"
pg.init()

screen = pg.display.set_mode((SCREEN_X, SCREEN_Y), 0)
""" background = pg.image.load(BG_FILE)
background = pg.transform.scale(background, (SCREEN_X, SCREEN_Y))
background.convert() """


boid = pg.image.load(BOID_FILE)
#boid = pg.transform.scale(boid, (10, 10))
hoik = pg.image.load(HOIK_FILE)
hoik = pg.transform.scale(hoik, (10, 10))
obstical = pg.image.load(OBSTICALS_FILE)
obstical = pg.transform.scale(obstical, (15, 15))

# Class Moves which makes the possition, speed
class Moving:
    
    def __init__(self):
        self.position = Vec2(random.randint(20, 800), random.randint(20, 600))
        self.velocity = Vec2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.velocity.normalize()
        
        self.perceived_distance = 100
        
    def move(self):
        self.position = self.position + self.velocity
        if self.position.x > SCREEN_X:
            self.position.x = 0
        if self.position.y > SCREEN_Y:
            self.position.y = 0
        if self.position.x < 0:
            self.position.x = SCREEN_X
        if self.position.y < 0:
            self.position.y = SCREEN_Y
    
    def update(self):
        self.position += self.velocity
        self.velocity.scale_to_length(2)
        self.move()
          
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
            avg_vec = Vec2(0, 0) # creates a vector with the value 0, 0
            for boid in local_boids: # for every boid in the local area
                avg_vec += boid.velocity # the average vector is added to the velocity of the boid
            avg_vec /= len(local_boids) # the average vector is divided by the number of boids in the local area
            self.velocity = (self.velocity + avg_vec) / 2 # the velocity of the boid is added to the average vector and divided by 2
            self.velocity.scale_to_length(2)  
        return self.velocity
    
    def cohesion(self, boids):
        """ 
        The cohesion function, is used to make the boids try to stay together, 
        by making the boids try to go to the center of the local boids (the gruop of boids)
        """
        local_boids = [] # List of boids in the local area
        for boid in boids: 
            if boid.position.distance_to(self.position) < self.perceived_distance: 
                local_boids.append(boid) # if the boid distance is smaller than the perceived distance append to the local boids
        if len(local_boids) > 0:
            avg_pos = Vec2(0, 0)
            for boid in local_boids: 
                avg_pos += boid.position # updating the average position by the boid position
            avg_pos /= len(local_boids)
            self.velocity += (avg_pos - self.position) / self.perceived_distance
            self.velocity.scale_to_length(2)
        return self.velocity
            
    """ def separation(self, boids):
        #The separation function, is used to make the boids 
        total = 0
        local_boids = []
        for boid in boids:
            distance = boid.position.distance_to(self.position)
            if self.position != boid.position and distance < self.perceived_distance:
                local_boids.append(boid) 
                diff = self.position - boid.position
                diff /= distance
                avg_vec = Vec2(0, 0)
                avg_vec += diff
                total += 1
        if total > 0:
            avg_vec /= total
            avg_vec = avg_vec.normalize() * 2
            steer = avg_vec - self.velocity
            steer.scale_to_length(1)
            self.velocity += steer
            self.velocity.scale_to_length(2)
        return self.velocity """   
    
    def separation(self, boids):
        local_boids = []
        for boid in boids:
            distance = boid.position.distance_to(self.position)
            if self.position != boid.position and distance < self.perceived_distance: 
                local_boids.append(boid) # if the boid is in the local area at a distance of 100
                avg_vec = Vec2(0,0) 
                
                difference = self.position - boid.position  # The difference between the boid and the other local boid
                difference /= distance  # The difference is divided by the distance
                avg_vec += difference # The average vector is added to the difference
        if len(local_boids) > 0:
            avg_vec /= len(local_boids)
            avg_vec = avg_vec.normalize()*2
            steer = avg_vec - self.velocity
            steer.scale_to_length(0.7)
            self.velocity += steer
            self.velocity.scale_to_length(2)
        return self.velocity
    

        
             
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
            obj.draw()
"""

class Boids(Moving): # In class Boids we will use the class Moves to move, for us the be availble to move something we need to first draw it
    
    def __init__(self):
        super().__init__()
    
    # Function wich rotate the triangle (boid) to the direction of the velocity
    def rotate(self):
        angle = math.degrees(-math.atan2(self.velocity.y, self.velocity.x)) - 45
        rotated_image = pg.transform.rotate(boid, angle) # Rotates the boid to the direction of the velocity vector 
        new_rect = rotated_image.get_rect(center=boid.get_rect(topleft=(self.position.x, self.position.y)).center)
        return rotated_image, new_rect
    
    def avoid_hoiks(self):
        for hoik in hoiks:
            distance = hoik.position.distance_to(self.position)
            if distance < 100:
                self.velocity += (self.position - hoik.position) / 100
                self.velocity.scale_to_length(2)
    
    # Function which draws the boid and the behaviour of the boid
    def draw_and_behaviour(self):
        boid, rect = self.rotate()
        self.move()
        self.update()
        self.alginment(boids) # This is the alginment function
        self.cohesion(boids) # This is the cohesion function
        self.separation(boids) # This is the separtion function
        self.avoid_hoiks()
        
        screen.blit(boid, (self.position.x, self.position.y))
        
    
class Hoiks(Moving):
    def __init__(self):
        super().__init__()
        
    # Add a function to rotate the hoik to the direction of the velocity
    
    # Function which makes the hoik hunt the boids
            

    def draw_and_behaviour(self):
        self.move()
        self.update()
                
        screen.blit(hoik, (self.position.x, self.position.y))
    

class obstacles(Moving):
    def __init__(self):
        super().__init__()
        
    def draw_and_behaviour(self):
        screen.blit(object, (self.position.x, self.position.y))


def draw():
    for boid in boids:
        boid.draw_and_behaviour()
    for hoik in hoiks:
        hoik.draw_and_behaviour()
    for obstacle in obstacles:
        obstacle.draw_and_behaviour()
        

boids = [Boids() for _ in range(20)]
hoiks = [Hoiks() for _ in range(10)]
obstacles = [obstacles() for _ in range(5)]

prev_time = time.time() * 1000
while True:
    now = time.time() * 1000
    if now - prev_time > 60: # 60 fps
        event = pg.event.poll()
        if event.type == pg.QUIT:
            break
        
        #screen.blit(background, (0,0))
        screen.fill([32,32,32])
        
        draw()
        
        pg.display.update()
        prev_time = now
print("Good bye, for now! ")
        