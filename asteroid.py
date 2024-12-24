from constants import *

import pygame, circleshape, random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        spawn_angle = random.uniform(20, 50)

        angle1 = self.velocity.rotate(spawn_angle)
        angle2 = self.velocity.rotate(-spawn_angle)

        new_ast1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_ast1.velocity = angle1 * 1.2

        new_ast2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_ast2.velocity = angle2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt