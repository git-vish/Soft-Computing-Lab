# STEP-1: defining sets
a = {0, 2, 4, 6, 8}
b = {1, 2, 3, 4, 5}

# STEP-2: generating results
print('A:', a)
print('B:', b)
print('\n1. A union B:', a | b)
print('2. A inter B:', a & b)
print('3. A - B:', a - b)
print('4. A sym diff B:', a ^ b)


'''
DESCRIPTION:
    All the Classical Set Operations are available in Python Standard library,
    so can be directly performed on 'set' type python objects
'''