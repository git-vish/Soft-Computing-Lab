"""
    AND-NOT Truth table for Bipolar inputs and targets

    x1      x2    AND-NOT
    -----------------------
    1       1       -1
    1      -1        1
   -1       1       -1
   -1      -1       -1
   We will initialize parameters with non-zero value and perform 3 epochs of training
"""

import numpy as np
import matplotlib.pyplot as plt

# STEP-1: initialize
X = np.array([(1, 1), (1, -1), (-1, 1), (-1, -1)])
Y = np.array([-1, 1, -1, -1])

# TODO: np.random.randn()
W = np.array([.2, .2])
b = .2
alpha = .2
E = []  # for saving errors
epochs = 5


# STEP-2: Learning
for epoch in range(epochs):
    temp_e = []  # for saving single example error
    print('Epoch:', epoch + 1)
    for x, y in zip(X, Y):
        y_in = round(W.dot(x.transpose()) + b, 2)
        e = y - y_in
        if e:
            W = np.round(W + alpha * e * x, 2)
            b = round(b + alpha * e, 2)
            e = round(e**2, 2)
            temp_e.append(e)
        print('x1={}, x2={}, y={}, y_in={}, w1={}, w2={}, b={}, error={}'.format(x[0], x[1], y, y_in, W[0], W[1], b, e))
    E.append(sum(temp_e))
    print('--------------------------------------')

print(E)
x_axis = range(1, len(E)+1)
plt.scatter(x_axis, E, color='r')
plt.legend('E')
plt.plot(x_axis, E, linestyle='--')
plt.xlabel('no. of epochs')
plt.ylabel('Error')
plt.show()

'''
DESCRIPTION
1. matplotlib.pyplot : library for visualization
         a)plt.scatter(): plots points
         b)plt.plot(): plots lines and curves
2. TODO
    For demonstration I've used fixed values from textbook ex: 7 page: 89
    You can replace it with following lines to create pure random values
        W = np.round(np.random.randn(2))
        b = np.round(np.random.random())

3. np.round(): function to round floating point vectors to given decimal

4. sum(): function takes iterable type argument and returns the sum of its elemets

'''
