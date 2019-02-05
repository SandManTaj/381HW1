import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

def nSidedDie(p):
    arr = np.array(p)
    if (np.sum(arr) != 1.0):
        sys.exit("Total probability is not 1!")
    arrsum = np.cumsum(arr)
    cp = np.append(0, arrsum)
    k = len(p)
    r = np.random.random()
    for i in range(0, k):
        if r > cp[i] and r <= cp[i+1]:
            d = i + 1
            return d

def main(): 

    a = np.array([0.10,  0.15,  0.20,  0.05,  0.30, 0.10, 0.10])
    m = 10000
    k = 7
    s = np.zeros((m,1))
    arrsum = np.cumsum(a)
    cp = np.append(0, arrsum)
    for i in range(0, m):
        d = nSidedDie(a)
        s[i] = d

    b = range(1,k+2)
    sb = np.size(b)
    h1, bins = np.histogram(s, bins=b)
    b1 = bins[0:sb-1]
    prob=h1/m
    plt.stem(b1,prob)
    plt.title('PMF for an unfair 7-sided die')
    plt.xlabel('Number on the face of the die')
    plt.ylabel('Probability')
    plt.xticks(b1)
    plt.show()

main()