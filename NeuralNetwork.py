from Matrix import Matrix

from random import random
from math import e


def sigmoid(x):
    return (e ** x) / (e ** x + 1)


def tanh(x):
    return (e ** x - e ** -x) / (e ** x + e ** -x)


def sign(x):
    return 0 if x < 0 else 1


class NeuralNetwork:
    """
    This class represents a genenal neural network.
    """

    def __init__(self, structure, learning_rate, activation_function=sigmoid):
        """
        Creates the neural network

        "structure" is an array, with each element being the number of neurons
        in each layer. Needs at least 2 elements for inputs and outputs.
        """

        # Saving informations about the structure for convenience
        self.structure = structure
        self.layers_count = len(self.structure)

        self.lr = learning_rate
        self.activation_function = activation_function

        # Creating layers
        self.layers = [Matrix(count, 1, init_value=0) for count in self.structure]

        # Creating weights
        self.weights = [
            Matrix(self.structure[i + 1], self.structure[i])
            for i in range(self.layers_count - 1)
        ]

        # Creating biases
        self.biases = [Matrix(self.layers[i].m, 1) for i in range(1, self.layers_count)]

        # Randomly initializing weights and biases
        for weight_mat in self.weights:
            weight_mat.set_data([random() for _ in range(weight_mat.m * weight_mat.n)])

        for biases_mat in self.biases:
            biases_mat.set_data([random() for _ in range(biases_mat.m * biases_mat.n)])

    @property
    def outputs(self):
        return self.layers[self.layers_count - 1]

    def activate(self, matrix):
        """
        Puts the matrix in the activation function "self.activation_function"
        """

        for i in range(matrix.m):
            for j in range(matrix.n):
                matrix[i][j] = self.activation_function(matrix[i][j])

    def guess(self, inputs):
        """
        Compute a guess with the neural network.

        "inputs" is a 1D array with the inputs data.

        The last layer of the self.layers is the outputs. Also returns the guess.
        """

        self.layers[0].set_data(inputs)

        for i in range(self.layers_count - 1):
            self.layers[i + 1] = self.weights[i] @ self.layers[i] + self.biases[i]

            self.activate(self.layers[i + 1])

        return self.outputs

    def train(self, inputs, targets):
        self.guess(inputs).data

        # Output layer

        targets_mat = Matrix(self.outputs.m, self.outputs.n)
        targets_mat.set_data(targets)

        error = targets_mat - self.outputs
        self.weights[self.layers_count - 2] += Matrix.element_multiply(
            error * self.lr,
            Matrix.element_multiply(
                self.outputs,
                Matrix(self.outputs.m, self.outputs.n, init_value=1) - self.outputs,
            ),
        ) @ Matrix.matrix_transpose(self.layers[self.layers_count - 2])

        for layer in range(self.layers_count - 2, 0, -1):
            error = Matrix.matrix_transpose(self.weights[layer]) @ error
            self.weights[layer - 1] += Matrix.element_multiply(
                error * self.lr,
                Matrix.element_multiply(
                    self.layers[layer],
                    Matrix(self.layers[layer].m, self.layers[layer].n, init_value=1)
                    - self.layers[layer],
                ),
            ) @ Matrix.matrix_transpose(self.layers[layer - 1])
