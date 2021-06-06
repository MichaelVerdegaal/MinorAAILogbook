from my_model import Model, Dense
from nn_functions import *


X_train = np.array([[0, 0, 1],
                    [1, 1, 1],
                    [1, 0, 1],
                    [0, 1, 1]])
y_train = np.array([[0, 1, 1, 0]]).T

model = Model(lr=0.01, loss_function=crossentropy)
model.add_layer(Dense(3, 10, ReLU()))
model.add_layer(Dense(10, 2, ReLU()))
model.add_layer(Dense(2, 1, Sigmoid()))


a = model.predict(X_train)

history = model.fit(X_train, y_train, epochs=10000)
print(f"\nMean loss: {np.mean(history)}")

b = model.predict(X_train)
print(f"\nExpected output: {y_train}")
print(f"\nPredictions before training: {a}")
print(f"\nPredictions after training: {b}")
