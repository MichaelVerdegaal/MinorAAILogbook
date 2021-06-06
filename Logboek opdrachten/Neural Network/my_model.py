import numpy as np
from nn_functions import mean_squared_error


class Model:
    def __init__(self, lr=0.01, loss_function=mean_squared_error):
        self.lr = lr
        self.layers = []
        self.loss_function = loss_function

    def add_layer(self, layer):
        self.layers.append(layer)

    def predict(self, inputs):
        result = np.array(inputs, ndmin=2)
        for layer in self.layers:
            result = layer.forward(result)
        return result

    def update_layer(self, layer, errors, lr):
        delta_weights = lr * np.dot(layer.outputs_no_activate.T,
                                    errors * layer.activation.differentiate(layer.outputs))
        layer.weights = np.add(layer.weights, delta_weights)
        delta_biases = lr * errors * layer.activation.differentiate(layer.outputs)
        layer.biases = np.add(layer.biases, delta_biases)

    def fit(self, inputs, labels, epochs=10):
        history = []
        for epoch in range(epochs):
            # Calculate loss
            loss = self.loss_function(self.predict(inputs), labels)
            history.append(loss)
            print(f"Epoch {epoch} | Loss: {loss}")

            # Calculate error
            o = self.predict(inputs)
            y = labels
            e = y - o

            for layer in reversed(self.layers):
                self.update_layer(layer, e, self.lr)
                # calculate hidden erorrs
                e = np.dot(e, layer.weights.T)
        return history


class Dense:
    def __init__(self, inputs, neurons, activation=None):
        self.weights = 0.10 * np.random.randn(inputs, neurons)
        self.biases = np.zeros((1, neurons))
        self.activation = activation
        self.outputs = []
        self.outputs_no_activate = []

    def forward(self, inputs):
        self.outputs_no_activate = inputs
        self.outputs = self.activation.calculate(np.dot(inputs, self.weights) + self.biases)
        return self.outputs
