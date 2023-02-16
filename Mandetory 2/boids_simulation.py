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
pg.display.set_caption("Boids, assignment 2")  # Name the window 
""" ----------------- Variables ----------------- """
# BOIDS
MAX_SPEED = 10
BOID_VELOCITY = 5
AVOID_HOIKS_DISTANCE = 100

# HOIKS
HUNT_DISTANCE = 100

# ALL OBJECTS
OBSTICAL_SIZE  = 10 
PERCEIVED_DISTANCE  = 200

""" --------------------------------------------- """

screen = pg.display.set_mode((SCREEN_X, SCREEN_Y), 0)

boid = pg.image.load(BOID_FILE)
hoik = pg.image.load(HOIK_FILE)
hoik = pg.transform.scale(hoik, (11, 11))
obstical = pg.image.load(OBSTICALS_FILE)


class Moving:
    """ 
    
    """ 
    def __init__(self):
        self.position = Vec2(random.randint(20, 800), random.randint(20, 600))
        self.velocity = Vec2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.velocity.normalize()
        
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
        Alignment function, is used to make the boids move in the same direction as the boids in the local area
        """
        local_boids = [] # List of boids in the local area
        for boid in boids: 
            if boid.position.distance_to(self.position) < PERCEIVED_DISTANCE : # if the boid is in the local area at a distance of 100
                local_boids.append(boid)
        if len(local_boids) > 0: # if there are boids in the local area
            avg_vec = Vec2(0, 0) # creates a vector with the value 0, 0
            for boid in local_boids: # for every boid in the local area
                avg_vec += boid.velocity # the average vector is added to the velocity of the boid
            avg_vec /= len(local_boids) * MAX_SPEED # the average vector is divided by the number of boids in the local area
            self.velocity = (self.velocity + avg_vec)  # the velocity of the boid is added to the average vector and divided by 2
            self.velocity.scale_to_length(BOID_VELOCITY)
        return self.velocity
    
    def cohesion(self, boids):
        """ 
        Cohesion function, is 
        """
        local_boids = [] # List of boids in the local area
        for boid in boids: 
            if boid.position.distance_to(self.position) < PERCEIVED_DISTANCE : 
                local_boids.append(boid) # if the boid distance is smaller than the perceived distance append to the local boids
        if len(local_boids) > 0:
            avg_pos = Vec2(0, 0)
            for boid in local_boids: 
                avg_pos += boid.position # updating the average position by the boid position
            avg_pos /= len(local_boids) 
            self.velocity += (avg_pos - self.position) / PERCEIVED_DISTANCE * 2
            self.velocity.scale_to_length(BOID_VELOCITY) 
        return self.velocity 
    

    def separation(self, boids):
        local_boids = []
        for boid in boids:
            distance = boid.position.distance_to(self.position)
            if self.position != boid.position and distance < PERCEIVED_DISTANCE : 
                local_boids.append(boid) # if the boid is in the local area at a distance of 100
                avg_vec = Vec2(0,0)
                
                difference = self.position - boid.position  # The difference between the boid and the other local boid
                difference /= distance  # The difference is divided by the distance
                avg_vec += difference # The average vector is added to the difference
        if len(local_boids) > 0:
            
            avg_vec /= len(local_boids)
            avg_vec = avg_vec.normalize()*2
            steer = avg_vec - self.velocity
            steer.scale_to_length(1)
            self.velocity += steer
            self.velocity.scale_to_length(BOID_VELOCITY)
        return self.velocity
    
    def hunt_to_eat(self):  # Hoiks hunt boids and eat them if impact
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
    In class Boids we will use the class Moves to move, 
    for us the be availble to move something we need to first draw it
    """
    def __init__(self):
        super().__init__()
    
    def rotate(self): # Rotates the triangle (boid) to the direction of the velocity
        angle = math.degrees(-math.atan2(self.velocity.y, self.velocity.x)) - 45
        rotated_image = pg.transform.rotate(boid, angle) 
        new_rect = rotated_image.get_rect(center=boid.get_rect(topleft=(self.position.x, self.position.y)).center)
        return rotated_image, new_rect
    
    def avoid_hoiks(self):
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
        self.alginment(boids) # This is the alginment function
        self.cohesion(boids) # This is the cohesion function
        self.separation(boids) # This is the separtion function
        self.avoid_obstacles()
    
        screen.blit(boid, (self.position.x, self.position.y))
        

class Hoiks(Moving):
    """ 
    
    """
    def __init__(self):
        super().__init__()
        self.boid = random.choice(boids)
        
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
    
    """
    def __init__(self):
        super().__init__()    
    
    def draw(self):
        screen.blit(obstical, (self.position.x, self.position.y))


def draw():
    for boid in boids:
        boid.draw_and_behaviour()
    for hoik in hoiks:
        hoik.draw_and_behaviour()
    for obstacle in obstacles:
       obstacle.draw()


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
        
        # If the B key is pressed the boids will be added to the list boids 

        screen.fill([32,32,32])
        
        draw()
        boids_counter(text_x, text_y)
        
        pg.display.update()
        prev_time = now
        
print("Good bye, for now! ")
        