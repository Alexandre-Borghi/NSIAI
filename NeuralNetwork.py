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

    def __init__(self, structure, activation_function=sigmoid):
        """
        Creates the neural network

        "structure" is a tuple, with each element being the number of neurons
        in each layer. Needs at least 2 elements for inputs and outputs.
        """

        # Saving informations about the structure for convenience
        self.structure = structure
        self.layers_count = len(self.structure)

        self.activation_function = activation_function

        # Creating layers
        self.layers = [Matrix(count, 1, init_value=0) for count in self.structure]

        # Creating weights
        self.weights = [
            Matrix(self.structure[i + 1], self.structure[i])
            for i in range(self.layers_count - 1)
        ]

        # Randomly initializing weights
        for weight_mat in self.weights:
            weight_mat.set_data([random() for _ in range(weight_mat.m * weight_mat.n)])

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
            self.layers[i + 1] = self.weights[i] @ self.layers[i]

            self.activate(self.layers[i + 1])

        return self.outputs
