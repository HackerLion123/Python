import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    sub = []
    for i in range(len(n)):
        for j in range(0,len(n)):
            if n[i:j] != '':
                sub.append(int(n[i:j+1]))
    print(sub)
    return sum(sub)

if __name__ == '__main__':
    #fptr = open(, 'w')

    n = input()

    result = substrings(n)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
