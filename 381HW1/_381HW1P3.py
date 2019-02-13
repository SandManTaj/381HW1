import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

def main():
    N = 100000
    counter = 0
    for i in range(0, N):
        hits = 0
        for j in range(0, 100):
            if(random.randint(0,1) == 1):
                hits += 1
        if(hits == 50):
            counter += 1
    print("Probability: ", counter/N)

main()