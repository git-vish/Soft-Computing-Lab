import numpy as np

# STEP 1: initializing
X = np.array([(0, 0), (0, 1), (1, 0), (1, 1)])
# for hidden layer
W1 = np.array([(1, -1), (-1, 1)])
# for output layer
W2 = np.array([1, 1])

# STEP 2: defining activation function
activation = np.vectorize(lambda num: 1 if num >= 1 else 0)

# STEP 3: calculating activations of Layer-1
Y_in_1 = W1.dot(X.transpose())
X1 = activation(Y_in_1)

# STEP 4: calculating activation of Output layer
Y_in_2 = W2.dot(X1)
Y_hat = activation(Y_in_2)

# STEP 5: printing results
print('x1\tx2\txor')
for x, y in zip(X, Y_hat):
    print(x[0], '\t', x[1], '\t', y)


'''
DESCRIPTION
1. numpy: it'a a python library for numerical computation, with VECTORIZATION capabilities
            a) np.array(): creates vectors (numpy array)
            b) np.vectorize(): takes input a function and coverts to vectorized version
            c) .dot: applied on numpy array with another array as argument, return dot product of those arrays
            d) .transpose(): returns vector transpose 
'''