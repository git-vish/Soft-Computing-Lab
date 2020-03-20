# STEP-1 : initialize
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [0, 0, 0, 1]
W = []
Y_in = []
theta = 0
Y_hat = []


# STEP-2 : input weights
for i in range(2):
    W.append(int(input('Enter w'+str(i+1)+': ')))

# STEP-3 : calculate Y_in
for x in X:
    Y_in.append(x[0]*W[0] + x[1]*W[1])


# STEP-4 : find theta
for i in Y_in:
    temp = []
    for j in Y_in:
        if j >= i:
            temp.append(1)
        else:
            temp.append(0)
    if temp == Y:
        theta = i
        break

# STEP-5 : AND using theta
for y in Y_in:
    if y >= theta:
        Y_hat.append(1)
    else:
        Y_hat.append(0)

# STEP-6 : Print results
print('\nOutput of Neural Network for AND:')
print('x1', '\t', 'x2', '\t', 'x1 AND x2')
for i in range(4):
    print(X[i][0], '\t', X[i][1], '\t\t', Y_hat[i])
print('with threshold:', theta)
