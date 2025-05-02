import pygame
from ai.NeuralNetwork import NeuralNet

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.size = 30  # Size of the bird (will be a circle for now)
        self.brain = NeuralNet()
    
    def decide(self, game_state_inputs):
        output = self.brain.forward(game_state_inputs)
        if output > 0.5:
            self.jump()
            
    def jump(self):
        self.velocity = self.jump_strength
        
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), self.size) 