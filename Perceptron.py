import numpy as np

# STEP-1: initialize
X = np.array([(1, 1), (1, -1), (-1, 1), (-1, -1)])
Y = np.array([1, -1, -1, -1])
W = np.array([0, 0])
b = 0
alpha = 1
theta = 0
epoch = 3


# STEP-2: defining STEP activation function
def activation(y_in):
    if y_in > theta:
        return 1
    elif y_in == theta:
        return 0
    return -1


# STEP-3: Learning
for e in range(epoch):  # for epochs
    print('Epoch:', e+1)
    w_temp, b_temp = W, b
    for x, y in zip(X, Y):  # for single example
        y_in = W.dot(x) + b  # calculate y_in
        y_hat = activation(y_in)
        if y_hat != y:  # update weights
            W = W + alpha * x * y
            b = b + alpha * y
        print('x1={}, x2={}, y={}, y_hat={}, w1={}, w2={}, b={}'.format(x[0], x[1], y, y_hat, W[0], W[1], b))
        print('--------------------------------------')
    if (w_temp == W).all() and b_temp == b:
        break

# STEP-4: Printing results
print("\n--------------]RESULT[----------------")
print('\tw1 : {}, w2 : {}, b : {}'.format(W[0], W[1], b))
print("--------------------------------------")

'''
DESCRIPTION
:: NOTE: epochs set to 3 but, learning completes at 2 epochs
1. tuple.all(): function returns 1 if all values of a tuple are True otherwise returns 0   
'''
