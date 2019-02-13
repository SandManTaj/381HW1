import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

#function which simulates an unfair n sided dice roll
def nSidedDie(p):
    arr = np.array(p)                                                   #converts the probability array into a numpy array
    if (np.sum(arr) != 1.0):                                            #exits the program if the total probability is not 1
        sys.exit("Total probability is not 1!")
    arrsum = np.cumsum(arr)                                             #converts the array into a cumulative sum array
    cp = np.append(0, arrsum)                                           #adds a zero at the beginning of the cumulative array
    k = len(p)                                                          #stores the number of sides of the die
    r = np.random.random()                                              #generates a random decimal number between 0 and 1
    #loops through the array to determine what side the die landed on
    for i in range(0, k):
        if r > cp[i] and r <= cp[i+1]:                                  #if r is between the i th side and the i + 1 th side
            d = i + 1                                                   #then it return the i + 1 th side
            return d

def main(): 

    a = np.array([0.10,  0.15,  0.20,  0.05,  0.30, 0.10, 0.10])        #array to store probabilities
    m = 10000                                                           #number of dice rolls
    k = 7                                                               #number of faces on the die
    s = np.zeros((m,1))                                                 #creates an array and buffers it with 0s
    #loop which rolls virtual die m times
    for i in range(0, m):
        d = nSidedDie(a)
        s[i] = d

    #matplotlib graph setup
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