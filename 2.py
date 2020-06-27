import numpy as np
from random import seed
import matplotlib.pyplot as plt

def BinaryArray(n,m, prob):
    seed(0)
    x = np.empty([n, m])
    for i in range(n):
        for j in range(m):
            s = np.random.uniform(0,1)
            if s <= prob :
                x[i][j] = 1
            else:
                x[i][j] = 0
    return x

def HammingSimilarity(x,y):
    count = 0
    for i in range(x.size):
        if x[i] == 1 and y[i] == 1:
            count = count + 1
    return count/x.size

def showArrray(a, b):

    # create an nxn numpy array
    a = np.reshape(a, (45,45))
    b = np.reshape(b, (45,45))
    plt.subplot(121)
    # use imshow to plot the array
    plt.imshow(a,  # numpy array generating the image
               cmap='gray',  # color map used to specify colors
               interpolation='nearest'
               # algorithm used to blend square colors; with 'nearest' colors will not be blended
               )
    plt.xticks(range(45))
    plt.yticks(range(45))
    plt.title('Gray color map, no blending', y=1.02, fontsize=12)

    # the same array as above, but with different color map
    plt.subplot(122)
    plt.imshow(b, cmap='gray', interpolation='nearest')
    plt.xticks(range(45))
    plt.yticks(range(45))
    plt.title('Viridis color map, no blending', y=1.02, fontsize=12)
    #
    # # the same array as above, but with blending
    # plt.subplot(133)
    # plt.imshow(a, cmap='viridis', interpolation='bicubic')
    # plt.yticks([])
    # plt.xticks(range(n))
    # plt.title('Viridis color map, bicubic blending', y=1.02, fontsize=12)
    plt.show()

n = 2025
m = 100
vec1 = BinaryArray(n,m, 0.02)
vec2 = BinaryArray(n,m, 0.02)
print(vec1.shape)
Similarity1 = HammingSimilarity(vec1[:,0],vec2[:,0])

print(vec1[:,0].shape)
print(vec2[:,0])
print(Similarity1)
showArrray(vec1[:,0], vec2[:,0])
