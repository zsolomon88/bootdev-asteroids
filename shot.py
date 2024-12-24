from constants import *

import pygame, circleshape

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.velocity * dt

    def rotate(self, direction):
        self.rotation = direction