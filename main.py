import pygame
import sys

from game import Game
from settings import *


def main():
    # Initialize Pygame
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")

    # Limit FPS
    clock = pygame.time.Clock()

    # Create Game Object
    game = Game(screen)

    # Main Loop
    running = True

    while running:

        # Handle Events
        for event in pygame.event.get():

            # Close Window
            if event.type == pygame.QUIT:
                running = False

            # Send every event to Game class
            game.handle_events(event)

        # Update Game
        game.update()

        # Draw Everything
        game.draw()

        # Refresh Screen
        pygame.display.flip()

        # FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()