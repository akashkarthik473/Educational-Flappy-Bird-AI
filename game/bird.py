import pygame
from ai.NeuralNetwork import NeuralNet
import random

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.size = 30  # Size of the bird (will be a circle for now)
        self.brain = NeuralNet()
        self.fitness = 0  # Track fitness score
        self.time_alive = 0  # Track how long the bird has been alive
        self.pipes_passed = 0  # Track number of pipes passed
    
    def decide(self, game_state_inputs):
        output = self.brain.forward(game_state_inputs)
        if output > 0.5:
            self.jump()
            
    def jump(self):
        self.velocity = self.jump_strength
        
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        self.time_alive += 1  # Increment time alive
        
    def draw(self, screen):
        # Draw bird with color based on fitness
        # Higher fitness = more green, lower fitness = more red
        fitness_color = min(255, int(self.fitness * 25))  # Scale fitness to color
        color = (255 - fitness_color, fitness_color, 0)  # RGB color based on fitness
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.size)
        
    def calculate_fitness(self):
        """Calculate the bird's fitness based on time alive and pipes passed"""
        # Base fitness on time alive and pipes passed
        # Pipes passed is weighted more heavily as it's a better indicator of success
        self.fitness = self.time_alive + (self.pipes_passed * 100)
        return self.fitness
        
    def clone(self):
        """Create a copy of this bird with the same neural network weights"""
        new_bird = Bird(self.x, self.y)
        new_bird.brain = self.brain.clone()
        return new_bird
        
    def mutate(self, mutation_rate=0.1):
        """Randomly mutate the bird's neural network weights"""
        self.brain.mutate(mutation_rate) 