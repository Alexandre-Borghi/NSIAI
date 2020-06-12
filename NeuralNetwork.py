from Matrix import Matrix

from random import random


class NeuralNetwork:
    """
    This class represents a genenal neural network.
    """

    def __init__(self, inputs, hidden_layers, outputs):
        """
        Creates the neural network

        inputs and outputs are ints, the number of inputs and outputs of the neural network.
        hidden_layers is a tuple, each element is the number of neurons in the respective layer.
        """

        # Saving informations about the structure for convenience
        self.inputs_count = inputs
        self.layers_count = hidden_layers
        self.outputs_count = outputs

        self.structure = (
            [self.inputs_count] + list(self.layers_count) + [self.outputs_count]
        )

        # Creating layers
        self.inputs = Matrix(self.inputs_count, 1, init_value=0)
        self.hidden_layers = [
            Matrix(count, 1, init_value=0) for count in self.layers_count
        ]
        self.outputs = Matrix(self.outputs_count, 1, init_value=0)

        # Creating weights
        self.weights = [
            Matrix(self.structure[i + 1], self.structure[i])
            for i in range(len(self.structure) - 1)
        ]

        # Randomly initializing weights
        for weight_mat in self.weights:
            weight_mat.set_data(random() for _ in range(weight_mat.m * weight_mat.n))
            weight_mat.display()


nn = NeuralNetwork(2, (), 1)

print(nn)
