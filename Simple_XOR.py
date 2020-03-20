# STEP 1: Defining Data
X1 = [0, 0, 1, 1]
X2 = [0, 1, 0, 1]

# STEP 2: Generating Results
print('x1\tx2\txor')
for x1, x2 in zip(X1, X2):
    print(x1, '\t', x2, '\t', x1 ^ x2)


'''
DESCRIPTION
1. ^ : bit-wise XOR function
2. zip() : takes multiple arguments of type iterable and combines them and returns an object of zip type
    eg. a = [1, 2, 3]
        b = ['a', 'b', 'c']
        zip(a, b) = |1, 'a'|, |2, 'b'|, ....
'''