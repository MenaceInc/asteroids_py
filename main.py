import sys
import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    clock = pygame.time.Clock()
    time_delta = 0

    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updateable = pygame.sprite.Group()

    Shot.containers = (shots, drawable, updateable)

    Player.containers = (drawable, updateable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    Asteroid.containers = (asteroids, drawable, updateable)
    AsteroidField.containers = (updateable)

    asteroid_field = AsteroidField()


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")

        updateable.update(time_delta)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit(0)
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        
        time_delta = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
