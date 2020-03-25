import numpy as np
import matplotlib.pyplot as plt

# STEP-1: initialization
X = np.array([(0, 0), (0, 1), (1, 0), (1, 1)])
Y = np.array([[0], [1], [1], [0]])
Y_hat = None
W1 = np.random.uniform(size=(2, 2))
b1 = np.zeros((1, 2))
W2 = np.random.uniform(size=(2, 1))
b2 = np.zeros((1, 1))

epochs = 10000
alpha = .1
E = {'x': [], 'y': []}  # for plotting


# STEP-2: defining required functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


def compute_error(e):   # calculates mean squared error
    return (1 / 2) * sum(e ** 2)


# STEP-3: learning
for _ in range(1, epochs+1):
    # forward propagation
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)
    Y_hat = A2
    # backward propagation
    error = Y - A2
    d2 = error * sigmoid_derivative(A2)

    error_hidden_layer = d2.dot(W2.T)
    d1 = error_hidden_layer * sigmoid_derivative(A1)

    # updating parameters
    W2 += A1.T.dot(d2) * alpha
    b2 += np.sum(d2, axis=0, keepdims=True) * alpha
    W1 += X.T.dot(d1) * alpha
    b1 += np.sum(d1, axis=0, keepdims=True) * alpha

    # printing error and accuracy
    if _ % 1000 == 0:
        e = compute_error(error)
        E['y'].append(e)
        E['x'].append(_)
        print('Epoch:', _)
        print('loss:', e)
        print('-----------------------------')

# STEP-4: printing results
print('\nLearning Completed')
print('Results: ')
print('x1 \t x2 \t xor')
for x, y in zip(X, Y_hat):
    print(x[0], '\t', x[1], '\t', round(y[0], 3))

# STEP-5: visualization
plt.plot(E['x'], E['y'])
plt.title('Learning')
plt.xlabel('no. of Epochs')
plt.ylabel('Error')
plt.show()

'''
DESCRIPTION:
1. np.random.uniform(size=(row, col)) : similar to np.random.randn(), but returns uniformly distributed numbers
2. round(float, digits): round(1.265, 2) ==> 1.27 
'''
