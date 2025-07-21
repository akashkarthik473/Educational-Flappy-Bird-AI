# Flappy Bird AI (Neuroevolution)

A modern, professional implementation of Flappy Bird with AI agents that learn to play using simple neural networks and evolutionary strategies. Built with Python and Pygame, this project demonstrates neuroevolution and real-time visualization of agent learning.

## Features

- **Multiple AI agents**: 50 birds learn simultaneously, each with its own neural network.
- **Neuroevolution**: Birds evolve over generations using mutation and selection.
- **Real-time visualization**: Watch the learning process as it happens.
- **Performance metrics**: Tracks score, best fitness, generation, and birds alive.
- **Automatic reset**: Game resets and evolves when all birds die.

## Neural Network Architecture

- **Inputs (4):**
  - Horizontal distance to next pipe
  - Bird's vertical position (Y)
  - Bird's vertical velocity
  - Vertical position of the next pipe gap
- **Hidden layer:** 8 neurons, sigmoid activation
- **Output:** 1 value (if > 0.5, bird jumps)

## Project Structure

```
.
├── main.py               # Entry point, runs the game loop
├── requirements.txt      # Python dependencies
├── ai/
│   └── NeuralNetwork.py  # Neural network class for birds
├── game/
│   ├── __init__.py       # Game package init
│   ├── bird.py           # Bird agent logic and fitness
│   ├── game.py           # Main game logic, evolution, rendering
│   └── pipe.py           # Pipe obstacle logic
└── LICENSE               # MIT License
```

## Setup

1. **Python 3.8+ required**
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

```bash
python main.py
```

- Press **SPACE** to make all birds jump (for testing)
- Close the window to exit

## How It Works

1. Each bird observes the environment and makes decisions using its neural network.
2. Birds that survive longer and pass more pipes are considered more 'fit'.
3. When all birds die, the top performers are cloned and mutated to form the next generation.
4. The process repeats, and birds improve over generations.

## Contributing

Contributions are welcome! Please open issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details. 