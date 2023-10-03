import numpy as np
import random


class Perceptron:
    def __init__(self, size):
        self.inputs = []
        self.weights = []
        self.summary = 0
        self.bias = 1

        random.seed(size)

        for i in range(size):
            self.inputs.append(random.randint(-20, 20))
            self.weights.append(random.randint(-20, 20))

        self.weights = self.weighted_summary()

    def internal_sigmoid(self, z):
        return 1 / (1 + np.exp(-z))  # ** (-z))

    def weighted_summary(self):
        summary = np.dot(self.inputs, self.weights) + self.bias
        return summary

    def sigmoid(self):
        return self.internal_sigmoid(self.weighted_summary())
