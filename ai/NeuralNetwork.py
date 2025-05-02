import numpy as np

class NeuralNet:
    def __init__(self, input_size=4, hidden_size=5, output_size=1):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Random weight initialization
        self.w1 = np.random.randn(hidden_size, input_size)  # (5 x 4)
        self.w2 = np.random.randn(output_size, hidden_size)  # (1 x 5)

    def forward(self, inputs):
        # Convert input list to numpy array
        inputs = np.array(inputs).reshape(-1, 1)  # shape (4, 1)

        # Hidden layer
        z1 = np.dot(self.w1, inputs)  # shape (5, 1)
        a1 = self.sigmoid(z1)         # activation

        # Output layer
        z2 = np.dot(self.w2, a1)      # shape (1, 1)
        output = self.sigmoid(z2)     # activation

        return output[0, 0]            # return single float value

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def clone(self):
        # Copy weights to a new NN
        clone = NeuralNet(self.input_size, self.hidden_size, self.output_size)
        clone.w1 = np.copy(self.w1)
        clone.w2 = np.copy(self.w2)
        return clone

    def mutate(self, mutation_rate=0.1):
        # Apply Gaussian noise to weights
        self.w1 += np.random.randn(*self.w1.shape) * mutation_rate
        self.w2 += np.random.randn(*self.w2.shape) * mutation_rate
