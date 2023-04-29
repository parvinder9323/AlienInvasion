import sys

import pygame


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialise the game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and Mouse Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen
            pygame.display.flip()


if __name__ == '__main__':
    # Make the game Instance and Run the game.
    ai = AlienInvasion()
    ai.run_game()
