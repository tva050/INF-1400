import pygame as pg
from pygame import Vector2 as Vec2
import math
import random
import time

SCREEN_X = 800
SCREEN_Y = 600

BOID_FILE = r"Mandetory 2\Figures\navigate.png"
HOIK_FILE = r"Mandetory 2\Figures\hoik.png"
OBSTICALS_FILE = r"Mandetory 2\Figures\polygon.png"

pg.init()
pg.display.set_caption("Boids, assignment 2") # Sets the title of the window
""" ----------------- Variables ----------------- """
# BOIDS
MAX_SPEED = 10 # The max speed of the boids
BOID_VELOCITY = 5 # The velocity of the boids
AVOID_HOIKS_DISTANCE = 100 # The distance the boids should avoid the hoiks

# HOIKS
HUNT_DISTANCE = 100 # The distance the hoiks should hunt the boids


# ALL OBJECTS
OBSTICAL_SIZE  = 10 # The size of the obsticals
PERCEIVED_DISTANCE  = 200 # The distance the boids can see

""" --------------------------------------------- """

screen = pg.display.set_mode((SCREEN_X, SCREEN_Y), 0)

boid = pg.image.load(BOID_FILE)
hoik = pg.image.load(HOIK_FILE)
hoik = pg.transform.scale(hoik, (11, 11))
obstical = pg.image.load(OBSTICALS_FILE)


class Moving:
    """ 
    Class that contains the functions that are used by the boids and hoiks
    Source: https://betterprogramming.pub/boids-simulating-birds-flock-behavior-in-python-9fff99375118
    """ 
    def __init__(self):
        self.position = Vec2(random.randint(20, 800), random.randint(20, 600))
        self.velocity = Vec2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.velocity.normalize()
    
    # Makes boid and hoiks appear on the other side of the screen when they go out of the screen
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
    
    # Updates the position of the boid and hoik
    def update(self):
        self.position += self.velocity
        self.velocity.scale_to_length(2)
        self.move()
          
    def alginment(self, boids): # Make the boids move in the same direction as the other boids in the local area
        local_boids = [] # List of boids in the local area
        for boid in boids: 
            if boid.position.distance_to(self.position) < PERCEIVED_DISTANCE : # if the boid distance is smaller than the perceived distance append to the local boids
                local_boids.append(boid)
        if len(local_boids) > 0: 
            avg_vec = Vec2(0, 0)
            for boid in local_boids: 
                avg_vec += boid.velocity # the average vector is added to the velocity of the boid
            avg_vec /= len(local_boids) * MAX_SPEED # the average vector is divided by the number of boids in the local area and the max speed
            self.velocity = (self.velocity + avg_vec)   # The velocity is added to the average vector
            self.velocity.scale_to_length(BOID_VELOCITY) # The velocity is scaled to the boid velocity
        return self.velocity
    
    def cohesion(self, boids): # Make the boids move towards the center of the local area
        local_boids = [] 
        for boid in boids: 
            if boid.position.distance_to(self.position) < PERCEIVED_DISTANCE : 
                local_boids.append(boid) 
        if len(local_boids) > 0:
            avg_pos = Vec2(0, 0)
            for boid in local_boids: 
                avg_pos += boid.position 
            avg_pos /= len(local_boids) 
            self.velocity += (avg_pos - self.position) / PERCEIVED_DISTANCE * 2 
            self.velocity.scale_to_length(BOID_VELOCITY)  
        return self.velocity 
    
    def separation(self, boids): # Make the boids move away from the other boids in the local area (not collide)
        local_boids = []
        for boid in boids:
            distance = boid.position.distance_to(self.position)
            if self.position != boid.position and distance < PERCEIVED_DISTANCE : 
                local_boids.append(boid) # if the boid is in the local area at a distance of 100
                avg_vec = Vec2(0,0)
                
                difference = self.position - boid.position  # The difference between the boid and the other local boid
                difference /= distance  
                avg_vec += difference 
        if len(local_boids) > 0: 
            avg_vec /= len(local_boids)
            avg_vec = avg_vec.normalize()*2
            
            steer = avg_vec - self.velocity
            steer.scale_to_length(1)
            
            self.velocity += steer
            self.velocity.scale_to_length(BOID_VELOCITY)
        return self.velocity
    
    def hunt_to_eat(self):  # Hoiks hunt the boids and eat them if they collide
        for hoik in hoiks:
            distance = hoik.position.distance_to(self.boid.position)
            if distance < HUNT_DISTANCE:
                self.velocity += (self.boid.position - hoik.position) / HUNT_DISTANCE
                self.velocity.scale_to_length(2)
            for boid in boids:
                if (hoik.position - boid.position).length() < 12:
                    boids.remove(boid)
                    
    def avoid_obstacles(self): # Boids and hoiks avoide obstacles
        for obstacle in obstacles:
            distance = obstacle.position.distance_to(self.position)
            if distance < OBSTICAL_SIZE :
                self.velocity += (self.position - obstacle.position) * OBSTICAL_SIZE 
                self.velocity.scale_to_length(2)


class Boids(Moving): 
    """ 
    Class which contains the boids and the behaviour of the boids:
        def rotate: rotates the boid to the direction of the velocity
        def avoid_hoiks: makes the boids avoid the hoiks
        def draw_and_behaviour: draws the boids and makes them move and behave
    """
    def __init__(self):
        super().__init__()
    
    def rotate(self): # Rotates the triangle (boid) to the direction of the velocity vector
        angle = math.degrees(-math.atan2(self.velocity.y, self.velocity.x)) - 45
        rotated_image = pg.transform.rotate(boid, angle) 
        new_rect = rotated_image.get_rect(center=boid.get_rect(topleft=(self.position.x, self.position.y)).center)
        return rotated_image, new_rect
    
    def avoid_hoiks(self): # Boids avoid hoiks
        for hoik in hoiks:
            distance = hoik.position.distance_to(self.position)
            if distance < AVOID_HOIKS_DISTANCE:
                self.velocity += (self.position - hoik.position) / AVOID_HOIKS_DISTANCE
                self.velocity.scale_to_length(2)
            
    # Function which draws the boid and the behaviour of the boid
    def draw_and_behaviour(self):
        boid, rect = self.rotate()
        self.move()
        self.update()
        self.avoid_hoiks()
        self.alginment(boids) 
        self.cohesion(boids) 
        self.separation(boids) 
        self.avoid_obstacles()
    
        screen.blit(boid, (self.position.x, self.position.y))
        

class Hoiks(Moving):
    """ 
    class which contains the hoiks and the behaviour of the hoiks
        def rotate: rotates the hoik to the direction of the velocity
        def draw_and_behaviour: draws the hoik and makes it move and behave
    """
    def __init__(self):
        super().__init__()
        self.boid = random.choice(boids) # The hoik will hunt a random boid
        
    # Add a function to rotate the hoik to the direction of the velocity
    def rotate(self):
        angle = math.degrees(-math.atan2(self.velocity.y, self.velocity.x))
        rotated_image = pg.transform.rotate(hoik, angle)
        new_rect = rotated_image.get_rect(center=hoik.get_rect(topleft=(self.position.x, self.position.y)).center)
        return rotated_image, new_rect
                 
    # Function which draws the hoik and the behaviour of the hoik
    def draw_and_behaviour(self):
        hoik, rect = self.rotate()
        self.move()
        self.update()
        self.separation(hoiks) # don't want the hoiks to collide with each other
        self.hunt_to_eat()
        self.avoid_obstacles()
        
        screen.blit(hoik, (self.position.x, self.position.y))
    

class obstacles(Moving):
    """ 
    class which contains obstacles
        def draw: draws the obstacles
    """
    def __init__(self):
        super().__init__()    
    
    def draw(self):
        screen.blit(obstical, (self.position.x, self.position.y))


def draw(): # Function which draws the boids, hoiks and obstacles
    for boid in boids:
        boid.draw_and_behaviour()
    for hoik in hoiks:
        hoik.draw_and_behaviour()
    for obstacle in obstacles:
       obstacle.draw()

# Create the number of boids, hoiks and obstacles 
boids = [Boids() for _ in range(60)]
hoiks = [Hoiks() for _ in range(5)]
obstacles = [obstacles() for _ in range(10)]

font = pg.font.SysFont("impact", 20) 
text_x = 10
text_y = 10
# Function which calculates how many boids are not eaten 
def boids_counter(x ,y):
    counter = 0
    for boid in boids:
        if boid.position.x != -50:
            counter += 1
    text = font.render("Boids: " + str(counter), True, (255,255,255))
    screen.blit(text, (x,y))

    
prev_time = time.time() * 1000 
while True:
    now = time.time() * 1000
    if now - prev_time > 60: # 60 fps
        event = pg.event.poll()
        if event.type == pg.QUIT: 
            break
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE: # escape(Esc) will close the window
                break
       
        screen.fill([32,32,32]) 
        
        draw()
        boids_counter(text_x, text_y)
        
        pg.display.update()
        prev_time = now
        
print("Good bye, for now! ")
        