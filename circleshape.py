import pygame
from typing import Self

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: int):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt: int):
        # sub-classes must override
        pass

    def check_for_collisions(self, other: Self):
        distance = self.position.distance_to(other.position)
        if distance <= (self.radius + other.radius):
            #print(f'{self.position} {other.position}')
            return True
        else:
            return False
