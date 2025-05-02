import pygame
import random

class Pipe:
    def __init__(self, x, screen_height):
        self.x = x
        self.gap_height = 150  # Smaller gap for more challenge
        self.width = 70
        self.speed = 3
        
        # Randomize the gap position
        min_gap_position = 150  # Minimum distance from top
        max_gap_position = screen_height - 150  # Minimum distance from bottom
        self.gap_position = random.randint(min_gap_position, max_gap_position)
        
        # Add some randomness to the gap height
        self.gap_height = random.randint(160, 200)
        
    def update(self):
        self.x -= self.speed
        
    def draw(self, screen):
        # Draw top pipe
        pygame.draw.rect(screen, (0, 255, 0), 
                        (self.x, 0, self.width, self.gap_position - self.gap_height//2))
        # Draw bottom pipe
        pygame.draw.rect(screen, (0, 255, 0),
                        (self.x, self.gap_position + self.gap_height//2, 
                         self.width, screen.get_height()))
                         
    def get_rects(self):
        """Return the rectangles for collision detection"""
        top_pipe = pygame.Rect(self.x, 0, self.width, 
                             self.gap_position - self.gap_height//2)
        bottom_pipe = pygame.Rect(self.x, self.gap_position + self.gap_height//2,
                                self.width, 1000)  # Large enough to cover screen
        return top_pipe, bottom_pipe 