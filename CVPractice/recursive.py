import numpy as np


def factorial(x):
    if x==1:
        return 1
    
    return x*factorial(x-1)
#print(factorial(3))

str = "abcdefghijklmnopqrstuvwxyz"

def findCharInString(char, i=0):
    if str[i]== char:
        return i
    i+=1
    return findCharInString(char,i)


print(findCharInString("c"))



    
    


