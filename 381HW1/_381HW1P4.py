import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import random
import string

def randString(n):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(n))

def main():
    m = 80000   #passwords
    k = 7
    N = 1000    #repitions
    count = 0
    passwords = np.append(0, m)
    for i in range(0, m):
        passwords[i] = randString(4)
    for i in range(0, N):
        yourPass = randString(4)

    print("Done!")

main()

