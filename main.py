# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Player.containers = (drawable, updatable)
    Shot.containers = (shots, drawable, updatable)

    ply = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ast_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for entity in updatable:
            entity.update(dt)
        
        for entity in drawable:
            entity.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides(ply):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collides(shot):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

