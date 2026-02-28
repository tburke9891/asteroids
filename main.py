import pygame
import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shot import Shot

from logger import log_state, log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group() # Group to hold objects that can be updated
    drawable = pygame.sprite.Group() # Group to hold objects that can be drawn
    asteroids = pygame.sprite.Group() # Group to hold Asteroid instances
    shots = pygame.sprite.Group() # Group to hold Shot instances

    Asteroid.containers = (asteroids, updatable, drawable) # Set the containers for the Asteroid class
    Shot.containers = (shots, updatable, drawable) # Set the containers for the Shot class
    AsteroidField.containers = (updatable) # Set the containers for the AsteroidField class
    asteroid_field = AsteroidField() # Create an instance of the AsteroidField

    Player.containers = (updatable, drawable) # Set the containers for the Player class

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2) # Create a player instance
    
    dt = 0

    while True:
        log_state()
        
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)  # Update all updatable objects

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                return
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill() # Remove the shot from all groups

        screen.fill("black")  # Clear the screen with black

        for obj in drawable:
            obj.draw(screen)  # Draw all drawable objects

        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000  # Limit to 60 frames per second and get delta time in seconds


if __name__ == "__main__":
    main()
