from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

import pygame

def main():
    pygame.init()
    dt = 0
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField() 
    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                return
        dt = fps.tick(60) / 1000 # amount of time that has passed since last call in ms
        screen.fill(color=(0, 0, 0))
        
        # calculate units new position 
        for unit in updatable:
            unit.update(dt)
        # detect if giving the new positions there is a collision
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game Over!")
                pygame.quit()
                return
        # detect if there is a collision between bullet and astroid
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.detect_collision(bullet):
                    asteroid.split()
                    pygame.sprite.Sprite.kill(bullet)
                    continue
        # update units in gui in no collision is detected
        for unit in drawable:
            unit.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
