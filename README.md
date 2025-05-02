# Flappy Bird AI

A Flappy Bird implementation with AI learning capabilities using Pygame and Neural Networks. The game features multiple birds learning simultaneously through their own neural networks.

## Features

- Multiple birds (50) learning simultaneously
- Neural Network-based decision making
- Real-time visualization of learning process
- Score tracking and bird survival count
- Automatic game reset when all birds die

## Neural Network Architecture

Each bird has its own neural network with:
- 4 inputs:
  - Distance to next pipe
  - Bird's Y position
  - Bird's velocity
  - Pipe gap position
- 5 hidden neurons
- 1 output (jump or not jump)

## Setup

1. Make sure you have Python 3.8+ installed
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Game

To run the game:
```
python main.py
```

Controls:
- SPACE: Make all birds jump (useful for testing)
- Close window to exit

## Project Structure

- `main.py`: Main game file
- `game/`: Game-related modules
  - `bird.py`: Bird class with neural network implementation
  - `pipe.py`: Pipe obstacles implementation
  - `game.py`: Main game logic
- `ai/`: AI-related modules
  - `NeuralNetwork.py`: Neural network implementation

## How It Works

1. Each bird has its own neural network that makes decisions based on:
   - Distance to the next pipe
   - Current position and velocity
   - Position of the pipe gap

2. The neural network processes these inputs and decides whether to jump

3. Birds that survive longer have better neural network weights

4. The game automatically resets when all birds die, creating a new generation

## Future Improvements

- Implement genetic algorithm for evolving successful birds
- Add visual distinction between birds
- Track and display performance metrics
- Save and load successful neural networks
- Add more sophisticated learning algorithms 