import numpy as np

class NeuralNet:
    """
    Simple feedforward neural network for Flappy Bird AI agent.
    Architecture: 4 inputs, 1 hidden layer (8 neurons), 1 output.
    """
    def __init__(self, input_size=4, hidden_size=8, output_size=1):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Random weight initialization
        self.w1 = np.random.randn(hidden_size, input_size)  # (8 x 4)
        self.w2 = np.random.randn(output_size, hidden_size)  # (1 x 8)

    def forward(self, inputs):
        """Feedforward pass. Returns output in [0, 1]."""
        inputs = np.array(inputs).reshape(-1, 1)  # shape (4, 1)
        z1 = np.dot(self.w1, inputs)  # shape (8, 1)
        a1 = self.sigmoid(z1)
        z2 = np.dot(self.w2, a1)      # shape (1, 1)
        output = self.sigmoid(z2)
        return output[0, 0]

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def clone(self):
        """Return a deep copy of this neural network."""
        clone = NeuralNet(self.input_size, self.hidden_size, self.output_size)
        clone.w1 = np.copy(self.w1)
        clone.w2 = np.copy(self.w2)
        return clone

    def mutate(self, mutation_rate=0.01):
        """Apply Gaussian noise to weights for evolution."""
        self.w1 += np.random.randn(*self.w1.shape) * mutation_rate
        self.w2 += np.random.randn(*self.w2.shape) * mutation_rate
