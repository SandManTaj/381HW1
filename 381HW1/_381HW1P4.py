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
    passwords = list()
    
    for i in range(0, m):
        passwords.append(randString(4))
    for i in range(0, N):
        yourPass = randString(4)
        if(yourPass in passwords):
            count = count + 1
    print("Probability: ", count/N)
    passwords.clear()
    count = 0
    for i in range(0, m*k):
        passwords.append(randString(4))
    for i in range(0, N):
        yourPass = randString(4)
        if(yourPass in passwords):
            count = count + 1
    print("Probability: ", count/N)
    passwords.clear()
    
    count = 0
    for i in range(0, m*4):
        passwords.append(randString(4))
    for i in range(0, N):
        yourPass = randString(4)
        if(yourPass in passwords):
            count = count + 1
    print("Probability: ", count/N)


main()

