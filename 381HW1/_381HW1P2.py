import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

def main():
    N = 100000
    s = np.zeros((N,1))
    for i in range(0, N):
        die1 = 0
        die2 = 0
        rolls = 0
        while(die1 + die2 != 7):
            die1 = random.randint(1,7)
            die2 = random.randint(1,7)
            rolls = rolls + 1
        s[i] = rolls
    arrmax = np.max(s)
    b = range(1,int(arrmax) + 2)
    sb = np.size(b)
    h1, bins = np.histogram(s, bins=b)
    b1 = bins[0:sb-1]
    prob=h1/N
    plt.stem(b1,prob)
    plt.title('PMF for an unfair 7-sided die')
    plt.xlabel('Number of rolls')
    plt.ylabel('Number of times')
    plt.xticks(b1)
    plt.show()
main()