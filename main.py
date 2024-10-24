import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,)

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    dt = 0
    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color="black")
        for sprite in updatable:
            sprite.update(dt)
        for asteroid in asteroids:
            if player1.check_for_collisions(asteroid):
                print("Game over!")
                sys.exit(0)
            for shot in shots:
                if shot.check_for_collisions(asteroid):
                    asteroid.split()
                    shot.kill()
                
        for sprite in drawable:
            sprite.draw(screen=screen)
        
        for shot in shots:
            shot.draw(screen)
            shot.update(dt)
        pygame.display.flip()
        dt = clock.tick(60)/1000
    


if __name__ == "__main__":
    main()

