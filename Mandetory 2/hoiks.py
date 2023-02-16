from boids_simulation import Moving

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