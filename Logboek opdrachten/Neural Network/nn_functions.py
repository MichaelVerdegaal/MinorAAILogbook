import numpy as np


class Sigmoid:
    def calculate(self, x):
        return 1 / (1 + np.exp(-np.array(x)))

    def differentiate(self, x):
        x = self.calculate(np.array(x))
        return x * (1 - x)


class ReLU:
    def calculate(self, x):
        return np.maximum(0, x)

    def differentiate(self, x):
        x = self.calculate(x)
        return np.where(x < 0, 0, 1)


class Softmax:
    def calculate(self, output):
        x = output - output.max(axis=0, keepdims=True)
        y = np.exp(x)
        return y / y.sum(axis=0, keepdims=True)

    def differentiate(self, output):
        x = self.calculate(np.array(output))
        return x * (1 - x)


class Tanh:
    def calculate(self, x):
        e_pos = np.exp(x)
        e_neg = np.exp(-x)
        return (e_pos - e_neg) / (e_pos + e_neg)

    def differentiate(self, x):
        x = self.calculate(x)
        return 1 - np.power(x, 2)


def crossentropy(predicted, items, return_mean=True):
    samples = len(items)
    correct_confidences = None
    # Clip data to prevent division by 0
    y_pred_clipped = np.clip(items, 1e-7, 1 - 1e-7)
    if len(predicted.shape) == 1:
        correct_confidences = y_pred_clipped[range(samples), predicted]
    elif len(predicted.shape) == 2:
        correct_confidences = np.sum(y_pred_clipped * predicted, axis=1)
    losses = -np.log(correct_confidences)
    mean_loss = np.mean(losses)
    return mean_loss if return_mean else losses


def mean_squared_error(predicted, items):
    return np.square(np.subtract(items, predicted)).mean()
