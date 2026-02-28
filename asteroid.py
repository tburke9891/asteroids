import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    containers = () # This will be set to the groups that hold Asteroid instances in main.py
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):  
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        # Create random angles for the new asteroids
        angle = random.uniform(20,50) 
        new_velocity1 =self.velocity.rotate(angle)
        new_velocity2 = self.velocity.rotate(-angle)

        # Create two new asteroids with half the original radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_velocity1 * 1.2
        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_velocity2 * 1.2
