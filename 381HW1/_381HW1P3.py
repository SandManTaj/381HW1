import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

def main():
    N = 100000                                  #repitions
    counter = 0                                 #counter for the number of times 50 heads/tails have been flipped
    #outside loop which repeats experiment 100000 times
    for i in range(0, N):
        hits = 0                                #records the number of times 1 (heads) is flipped
        for j in range(0, 100):                 #inside loop to flip a fair coin 100 times
            if(random.randint(0,1) == 1):       
                hits += 1                       #increment the hits counter if 1(heads) is flipped
        if(hits == 50):
            counter += 1                        #increment the counter if after flipping a coin 100 times, 50 heads were flipped
    print("Probability: ", counter/N)           #prints out the probability

main()