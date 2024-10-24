from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            random_angle = random.uniform(20,50)
            angle1 = self.velocity.rotate(-random_angle)
            angle2 = self.velocity.rotate(random_angle)
            asteroid1 = Asteroid(self.position[0],self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            asteroid1.velocity = angle1 * 1.2
            asteroid2 = Asteroid(self.position[0],self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            asteroid2.velocity = angle2 * 1.2

        self.kill()



