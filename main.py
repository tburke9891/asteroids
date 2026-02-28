import pygame
import constants
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # Delta time for frame rate independence

    while True:
        log_state()
        
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")  # Clear the screen with black
        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000  # Limit to 60 frames per second

if __name__ == "__main__":
    main()
