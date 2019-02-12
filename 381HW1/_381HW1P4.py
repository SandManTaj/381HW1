import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import random
import string


def main():
    #initializations
    m = 80000                                                                                       #passwords
    k = 7                                                                                           #multiplier for the number of passwords
    N = 1000                                                                                        #repitions
    count = 0                                                                                       #counter for the number of matches
    passwords = list()                                                                              #list to store hacker passwords
    
    #loop to create 80000 passwords
    for i in range(0, m):
        passwords.append(''.join(random.choice(string.ascii_lowercase) for x in range(4)))          #creates a random string of length 4
    #loop to determine the number of matches in a list of 80000 passwords
    for i in range(0, N):
        yourPass = ''.join(random.choice(string.ascii_lowercase) for x in range(4))
        if(yourPass in passwords):
            count = count + 1                                                                       #increment the counter if some password in the list matches the key
    print("Probability: ", count/N)                                                                 #displays the probability
    passwords.clear()                                                                               #empties the list of passwords
    count = 0                                                                                       #resets the count for the next loop

    #loop to create 80000*7 passwords
    for i in range(0, m*k):
        passwords.append(''.join(random.choice(string.ascii_lowercase) for x in range(4)))          #creates a random string of length 4
    #loop to determine the number of matches in a list of 80000*7 passwords
    for i in range(0, N):
        yourPass = ''.join(random.choice(string.ascii_lowercase) for x in range(4))
        if(yourPass in passwords):
            count = count + 1                                                                       #increment the counter if some password in the list matches the key
    print("Probability: ", count/N)                                                                 #displays the probability
    passwords.clear()                                                                               #empties the list of passwords
    count = 0                                                                                       #resets the count for the next loop

    #loop to create 80000*4 passwords
    for i in range(0, m*4):
        passwords.append(''.join(random.choice(string.ascii_lowercase) for x in range(4)))          #creates a random string of length 4
    #loop to determine the number of matches in a list of 80000*4 passwords
    for i in range(0, N):
        yourPass = ''.join(random.choice(string.ascii_lowercase) for x in range(4))
        if(yourPass in passwords):
            count = count + 1                                                                       #increment the counter if some password in the list matches the key
    print("Probability: ", count/N)                                                                 #displays the probability


main()

