# My Machine Learning Project

# Example 1   0   0   1   -   0
# Example 2   1   1   1   -   1
# Example 3   1   0   1   -   1
# Example 4   0   1   1   -   0
#
# New Situation   1   0   0   -   ?

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_izvod(x):
    return x * (1 - x)


training_inputs = np.array([[0, 0, 1],
                            [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1]])

training_outputs = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3, 1)) - 1

print('Random starting synaptic weights: \n', synaptic_weights)

for iteration in range(20000):
    input_layer = training_inputs
    output_layer = sigmoid(np.dot(input_layer, synaptic_weights))

    error = training_outputs - output_layer
    adjustments = error * sigmoid_izvod(output_layer)
    synaptic_weights += np.dot(input_layer.T, adjustments)

print('Synaptic weights after training: \n', synaptic_weights)

print('Outputs after training: \n', output_layer)

# print(sigmoid(-0.99977125))
