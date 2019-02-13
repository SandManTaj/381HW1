import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

def main():
    N = 100000                                      #number of repitions
    s = np.zeros((N,1))                             #creates an array and appends zeros to it
    #loop to roll the dice N times
    for i in range(0, N):
        die1 = 0                                    #creates first die
        die2 = 0                                    #creates second die
        rolls = 0                                   #counter for the number of rolls needed to roll 7
        #loops until 7 is rolled, increments the counter each loop
        while(die1 + die2 != 7):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            rolls = rolls + 1
        s[i] = rolls                                #stores the number of rolls necessary
    #matplotlib graph
    arrmax = np.max(s)
    b = range(1,int(arrmax) + 2)
    sb = np.size(b)
    h1, bins = np.histogram(s, bins=b)
    b1 = bins[0:sb-1]
    prob=h1/N
    plt.stem(b1,prob)
    plt.title('PMF for an unfair 7-sided die')
    plt.xlabel('Number of rolls')
    plt.ylabel('Probability')
    plt.xticks(b1)
    plt.show()
main()