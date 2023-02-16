from boids_simulation import Moving

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

