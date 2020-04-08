# STEP-1: defining functions
def union(fs1, fs2):  # A U B = max(mA, mB)
    temp = []
    for i in range(len(fs1)):
        if fs1[i][0] > fs2[i][0]:
            temp.append(fs1[i])
        else:
            temp.append(fs2[i])
    return temp


def intersection(fs1, fs2):  # A inter B = min(mA, mB)
    temp = []
    for i in range(len(fs1)):
        if fs1[i][0] < fs2[i][0]:
            temp.append(fs1[i])
        else:
            temp.append(fs2[i])
    return temp


def compliment(fs):  # A' = 1 - mA(x)
    temp = []
    for i in fs:
        e = 1 - i[0]
        temp.append([e, i[1]])
    return temp


def difference(fs1, fs2):  # A - B = A inter B'
    return intersection(fs1, compliment(fs2))


# STEP-2: performing Operations
a = [[1, 2], [0.3, 4], [0.5, 6], [0.2, 8]]
b = [[0.5, 2], [0.4, 4], [0.1, 6], [1, 8]]

print("A:", a)
print("B:", b)
print('\n1. A union B:', union(a, b))
print('2. A inter B:', intersection(a, b))
print("3. A':", compliment(a))
print("4. B':", compliment(b))
print('5. A - B:', difference(a, b))
print('6. B - A:', difference(b, a))
