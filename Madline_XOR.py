import numpy as np

# STEP-1: initialize
X = np.array([(1, 1), (1, -1), (-1, 1), (-1, -1)])
Y = np.array([-1, 1, 1, -1])
# for hidden layer
W = np.array([(0.05, 0.2), (0.1, 0.2)])
b = np.array([[0.3], [0.15]])
# for output layer
V = np.array([0.5, 0.5])
b2 = 0.5
# learning rate
alpha = 0.5
# no. of epochs
epochs = 5

# STEP-2: defining required functions
activation = np.vectorize(lambda num: 1 if num >= 0 else -1)
is_positive = np.vectorize(lambda num: 1 if num >= 0 else 0)


def closets_to_zero(z):  # return index of Z which is closest to 0
    a = [abs(e) for e in z]
    return a.index(min(a))


# STEP-3: learning
for epoch in range(epochs):
    print('Epoch:', epoch + 1)
    w_temp, b_temp = W, b
    for x, y in zip(X, Y):
        x = x.reshape(-1, 1)
        Z = W.dot(x) + b  # hidden layer net i/p
        A = activation(Z)  # hidden layer activation
        y_in = V.T.dot(A) + b2  # output layer net i/p
        y_hat = activation(y_in)  # output layer activation
        if y != y_hat:
            if y == 1:
                i = closets_to_zero(Z)
                W[i] = W[i] + alpha * (1 - Z[i]) * x.T
                b[i] = b[i] + alpha * (1 - Z[i])
            else:
                p = is_positive(Z)
                if p.all():
                    W = W + alpha * (-1 - Z) * x
                    b = b + alpha * (-1 - Z)
                else:
                    i = p.index(1)
                    W[i] = W[i] + alpha * (-1 - Z[i]) * x
                    b[i] = b[i] + alpha * (-1 - Z[i])
        print('x1={}, x2={}, z1={}, z2={}, a1={}, a2={}, y={}, y_hat={}, w11={}, w21={}, b1={}, w12={}, w22={}, b2={}'
              .format(x[0], x[1], Z[0], Z[1], A[0], A[1], y, y_hat, W[0][0], W[0][1], W[1][0], W[1][1], b[0], b[1]))
        print('--------------------------------------')
    if (W == w_temp).all() and (b == b_temp).all():
        break

# STEP-4: printing results
print("\n--------------]RESULT[----------------")
print(
    '\tw11 : {}, w21 : {}, b1 : {}, w21 : {}, w22 : {}, b2 : {}'.format(W[0][0], W[0][1], b[0], W[1][0], W[1][1], b[1]))
print("--------------------------------------")


# STEP-5: prediction
def predict():
    print('\nXOR for bipolar inputs and targets')
    x_test = np.array([int(input('Enter x1: ')), int(input('Enter x2: '))])
    x_test = x_test.reshape(-1, 1)
    z_test = W.dot(x_test) + b
    a_test = activation(z_test)
    z_test = V.T.dot(a_test) + b2
    a_test = activation(z_test)
    print('XOR:', a_test[0])


predict()

'''
DESCRIPTION:
:: NOTE: epochs set to 5 but, learning completes at 3 epochs
1. abs(): 
    function takes input of type number or iterable of numbers and returns absolute values
2. index():
    function takes input a element and return it's position in iterable if present
3. reshape():
    function of numpy array, take input the desired shape
        e.g. if a.shape = (3, )
                a.reshape(-1, 1) will cause
                a.shape = (3, 1)
        :: NOTE : -1 is used as it will detect the dimension automatically
4. T:
    function to transpose vector
    a.T == a.transpose()
'''
