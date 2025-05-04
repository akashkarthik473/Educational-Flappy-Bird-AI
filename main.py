import pygame
import sys
from game.game import Game

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird AI - 50 Birds")

# Create game instance with 50 birds
game = Game(WINDOW_WIDTH, WINDOW_HEIGHT, num_birds=50)

# Game loop
def main():
    clock = pygame.time.Clock()
    
    while True:
        # Handle input
        if not game.handle_input():
            pygame.quit()
            sys.exit()
        
        # Update game state
        game.update()
        
        # Draw everything
        game.draw(screen)
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()  