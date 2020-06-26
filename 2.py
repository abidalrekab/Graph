import numpy as np

def BinaryArray(n, prob):
    x = np.empty(n)
    xnew = np.empty(n)
    for i in range(n):
        s = np.random.uniform(0,1)
        xnew[i] = np.random.choice([-1,1], p = [prob, 1-prob])
        if s <= prob :
            x[i] = 1
        else:
            x[i] = -1
    return x, xnew

def HammingSimilarity(x,y):
    count = 0
    for i in range(x.size):
        if x[i] == y[i]:
            count = count + 1
    return count/x.size
n = 2048
vec1, vec11 = BinaryArray(n, 0.02)
vec2, vec22 = BinaryArray(n, 0.02)
Similarity1 = HammingSimilarity(vec1,vec2)
Similarity2 = HammingSimilarity(vec11,vec22)
#print('the number of combinations', pow(2,n))
print(vec1)
print(vec2)
print(Similarity1)
print(Similarity2)

