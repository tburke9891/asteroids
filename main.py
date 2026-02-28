import constants
import player
import pygame

from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # Delta time for frame rate independence
    player1 = player.Player(x = constants.SCREEN_WIDTH / 2, y = constants.SCREEN_HEIGHT / 2)

    while True:
        log_state()
        
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")  # Clear the screen with black
        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000  # Limit to 60 frames per second
        player1.draw(screen)  # Draw the player
        player1.update(dt)  # Update the player's state

if __name__ == "__main__":
    main()
