# STEP-1: Defining FuzzySet class with its operations using operator overloading
class FuzzySet:
    def __init__(self, fs):
        self.fs = fs

    def __len__(self):
        return len(self.fs)

    def __or__(self, other):    # union(A, B) = max(mA, mB)
        assert len(self) == len(other), "Both Fuzzy Sets must have same length"
        fs2 = other.fs
        temp = []
        for i in range(len(self.fs)):
            if self.fs[i][0] > fs2[i][0]:
                temp.append(self.fs[i])
            else:
                temp.append(fs2[i])
        return FuzzySet(temp)

    def __and__(self, other):   # intersection(A, B) = min(mA, mB)
        assert len(self) == len(other), "Both Fuzzy Sets must have same length"
        fs2 = other.fs
        temp = []
        for i in range(len(self.fs)):
            if self.fs[i][0] < fs2[i][0]:
                temp.append(self.fs[i])
            else:
                temp.append(fs2[i])
        return FuzzySet(temp)

    def __invert__(self):   # compliment(A) = 1 - mA(x)
        temp = []
        for i in self.fs:
            e = 1 - i[0]
            temp.append([e, i[1]])
        return FuzzySet(temp)

    def __sub__(self, other):   # A-B = intersection(A, compliment(B))
        assert len(self) == len(other), "Both Fuzzy Sets must have same length"
        return self.__and__(other.__invert__())

    def __str__(self):
        return str(self.fs)


# STEP-2: Declaring FuzzySets
a = FuzzySet([[1, 2], [0.3, 4], [0.5, 6], [0.2, 8]])
b = FuzzySet([[0.5, 2], [0.4, 4], [0.1, 6], [1, 8]])

# STEP-3: Generating results
print("A:", a)
print("B:", b)
print('\n1. A union B:', a | b)
print('2. A inter B:', a & b)
print("3. A':", ~a)
print("4. B':", ~b)
print('5. A - B:', a - b)
print('6. B - A:', b - a)


'''
DESCRIPTION:
    In class FuzzySet we have overloaded some operators to represent FuzzySet Operations
    In Python operator are overloaded using there associated methods
    e.g.    & -> __and__()
            | -> __or__()
            - -> __sub__() etc.
    __str__() method is similar to toString() in other languages, which return String format of the calling object 
    object.__len__() method is called when len(object) is called, return length of object
    assert is a keyword used to raise exception if the given condition not satisfied
'''
