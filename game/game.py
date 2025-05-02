import pygame
from game.bird import Bird
from game.pipe import Pipe

class Game:
    def __init__(self, width, height, num_birds=50):
        self.width = width
        self.height = height
        self.num_birds = num_birds
        self.generation = 1  # Move generation to class level
        self.best_fitness = 0  # Move best_fitness to class level
        self.reset_game()
        
    def reset_game(self):
        self.birds = [Bird(self.width // 4, self.height // 2) for _ in range(self.num_birds)]
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.pipe_spawn_timer = 0
        self.pipe_spawn_delay = 90  # Frames between pipe spawns
        self.passed_pipes = set()  # Keep track of pipes we've passed
        
    def get_next_pipe(self):
        """Returns the next pipe the bird needs to pass through"""
        if not self.pipes:
            return None
            
        # Find the first pipe that hasn't been passed yet
        for pipe in self.pipes:
            if pipe not in self.passed_pipes:
                return pipe
        return None
        
    def get_distance_to_next_pipe(self):
        """Returns the horizontal distance to the next pipe"""
        next_pipe = self.get_next_pipe()
        if next_pipe is None:
            return self.width  # If no pipe, return screen width
            
        # Calculate distance from bird to pipe
        distance = next_pipe.x - self.birds[0].x  # Use first bird as reference
        return distance
        
    def get_game_state_inputs(self, bird):
        """Returns the inputs for the neural network for a specific bird"""
        next_pipe = self.get_next_pipe()
        if next_pipe is None:
            return [
                self.width / 800,  # Normalized distance to pipe
                bird.y / 600,  # Normalized bird y position
                bird.velocity / 10,  # Normalized velocity
                self.height / 2 / 600  # Normalized gap position
            ]
            
        return [
            (next_pipe.x - bird.x) / 800,  # Normalized distance to pipe
            bird.y / 600,  # Normalized bird y position
            bird.velocity / 10,  # Normalized velocity
            next_pipe.gap_position / 600  # Normalized gap position
        ]
        
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Make all birds jump when space is pressed
                    for bird in self.birds:
                        bird.jump()
        return True
        
    def update(self):
        # Update all birds
        for bird in self.birds:
            bird.update()
            # Let each bird think about the game state
            game_state_inputs = self.get_game_state_inputs(bird)
            bird.decide(game_state_inputs)
        
        # Update pipes
        for pipe in self.pipes:
            pipe.update()
            
        # Remove off-screen pipes
        self.pipes = [pipe for pipe in self.pipes if pipe.x > -pipe.width]
        
        # Spawn new pipes
        self.pipe_spawn_timer += 1
        if self.pipe_spawn_timer >= self.pipe_spawn_delay:
            new_pipe = Pipe(self.width, self.height)
            self.pipes.append(new_pipe)
            self.pipe_spawn_timer = 0
            
        # Check collisions for all birds
        for bird in self.birds[:]:  # Create a copy of the list to safely remove birds
            # Check pipe collisions
            for pipe in self.pipes:
                if self.check_collision(bird, pipe):
                    bird.calculate_fitness()  # Calculate final fitness before removing
                    self.best_fitness = max(self.best_fitness, bird.fitness)
                    self.birds.remove(bird)
                    break
                    
            # Check ground/ceiling collisions
            if bird.y <= 0 or bird.y >= self.height:
                bird.calculate_fitness()  # Calculate final fitness before removing
                self.best_fitness = max(self.best_fitness, bird.fitness)
                self.birds.remove(bird)
                
        # If all birds are dead, reset the game
        if not self.birds:
            self.game_over = True
            print(f"Generation {self.generation} complete!")
            print(f"Best fitness: {self.best_fitness}")
            print(f"Score: {self.score}")
            self.generation += 1  # Increment generation before reset
            self.reset_game()
            return
            
        # Update score and track pipes passed
        for pipe in self.pipes:
            # Only score if we haven't passed this pipe before
            if pipe not in self.passed_pipes and self.birds[0].x > pipe.x + pipe.width:
                self.score += 1
                self.passed_pipes.add(pipe)
                # Increment pipes_passed for all alive birds
                for bird in self.birds:
                    bird.pipes_passed += 1
                
        # Update fitness for all alive birds
        for bird in self.birds:
            bird.calculate_fitness()
                
    def check_collision(self, bird, pipe):
        bird_rect = pygame.Rect(bird.x - bird.size, 
                              bird.y - bird.size,
                              bird.size * 2, bird.size * 2)
        
        top_pipe, bottom_pipe = pipe.get_rects()
        return bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe)
        
    def draw(self, screen):
        screen.fill((135, 206, 235))  # Sky blue background
        
        # Draw pipes
        for pipe in self.pipes:
            pipe.draw(screen)
            
        # Draw all birds
        for bird in self.birds:
            bird.draw(screen)
        
        # Draw score and bird count
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        birds_text = font.render(f'Birds Alive: {len(self.birds)}', True, (255, 255, 255))
        generation_text = font.render(f'Generation: {self.generation}', True, (255, 255, 255))
        fitness_text = font.render(f'Best Fitness: {self.best_fitness}', True, (255, 255, 255))
        
        screen.blit(score_text, (10, 10))
        screen.blit(birds_text, (10, 50))
        screen.blit(generation_text, (10, 90))
        screen.blit(fitness_text, (10, 130))