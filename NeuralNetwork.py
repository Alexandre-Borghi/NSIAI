from Matrix import Matrix

from random import random
import math
from math import e, cosh


def sigmoid(x):
    return 1 / (1 + e ** (-x))


def d_sigmoid(x):
    return x * (1 - x)


def tanh(x):
    return math.tanh(x)


def d_tanh(x):
    try:
        return 1 / (cosh(x) * cosh(x))
    except OverflowError:
        print("Overflowed")
        return float("1.7976931348623157e+307")


class NeuralNetwork:
    """
    This class represents a genenal neural network.
    """

    def __init__(self, structure, learning_rate, activation=tanh, derivative=d_tanh):
        """
        Creates the neural network

        "structure" is an array, with each element being the number of neurons
        in each layer. Needs at least 2 elements for inputs and outputs.
        """

        # Saving informations about the structure for convenience
        self.structure = structure
        self.layers_count = len(self.structure)

        self.lr = learning_rate
        self.activation = activation
        self.derivative = derivative

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

    def map(self, matrix, function):
        """
        Maps the function to every element of the matrix and returns the new matrix without modifying the parameter
        """

        new_mat = Matrix(matrix.m, matrix.n)

        for i in range(matrix.m):
            for j in range(matrix.n):
                new_mat[i][j] = function(matrix[i][j])

        return new_mat

    def activate(self, matrix):
        """
        Maps the activation function to every element of the matrix
        """

        for i in range(matrix.m):
            for j in range(matrix.n):
                matrix[i][j] = self.activation(matrix[i][j])

    def guess(self, inputs):
        """
        Compute a guess with the neural network.

        "inputs" is a 1D array with the inputs data.

        The last layer of the self.layers is the outputs. Also returns the guess.
        """

        self.layers[0].set_data(inputs)

        for i in range(self.layers_count - 1):
            self.layers[i + 1] = (self.weights[i] @ self.layers[i]) + self.biases[i]

            self.activate(self.layers[i + 1])

        return self.outputs

    def train(self, inputs, targets):
        self.guess(inputs)

        targets_mat = Matrix(self.outputs.m, self.outputs.n)
        targets_mat.set_data(targets)

        error = None

        # delta_weights = lr * ERROR * layer' * activated_layer-1(T)

        for layer in range(self.layers_count - 1, 0, -1):
            if layer == self.layers_count - 1:  # Calculate error from targets
                error = targets_mat - self.outputs
            else:
                error = Matrix.matrix_transpose(self.weights[layer]) @ error

            derivative_mat = self.map(self.layers[layer], self.derivative)

            transposed_mat = Matrix.matrix_transpose(self.layers[layer - 1])

            delta_weights = Matrix.element_multiply(derivative_mat, error)
            delta_weights *= self.lr

            self.biases[layer - 1] += delta_weights

            delta_weights @= transposed_mat

            self.weights[layer - 1] += delta_weights
