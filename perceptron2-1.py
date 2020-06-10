from random import *
from math import e

def sigmoid(x):
    return (e**x) / (e**x + 1)

def tanh(x):
    return (e**x - e**-x) / (e**x + e**-x)

def sign(x):
    return 0 if x < 0 else 1

class Perceptron2:
    """
    Cette classe représente un réseau de neurones à :
        - 2 entrées
        - 1 sortie
    """
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.bias = 1
        self.w0 = random()
        self.w1 = random()
        self.wbias = random()
        self.output = 0

        self.lr = 0.1

        self.activation = sign
    
    def predict(self, x1, x2):
        """
        Cette fonction prend une entrée x et retourne la prédiction du perceptron
        """
        self.input1 = x1
        self.input2 = x2
        self.output = self.activation(self.input1 * self.w0 + self.input2 * self.w1 + self.bias * self.wbias)
        self.summary()
    
    def train(self, x1, x2, y):
        self.predict(x1, x2)
        error = y - self.output

        self.w0 += error * self.lr * x1
        self.w1 += error * self.lr * x2
        self.wbias += error * self.lr * self.bias

    
    def summary(self):
        print("Inputs : {0:.10f}, {1:.10f} | Output : {2:.10f}".format(self.input1, self.input2, self.output))

nn = Perceptron2()

data = [
    [0.0, 0.0, 0.0],
    [0.0, 1.0, 1.0],
    [1.0, 0.0, 1.0],
    [1.0, 1.0, 1.0]
]

for epoch in range(5):
    for batch in range(1000):
        training_data = data[randint(0, 3)]
        nn.train(training_data[0], training_data[1], training_data[2])
    
    nn.lr /= 10

print("\n-----------------------------------\n")

nn.predict(0, 0)
nn.predict(0, 1)
nn.predict(1, 0)
nn.predict(1, 1)

nn.predict(0.23, 0.459)