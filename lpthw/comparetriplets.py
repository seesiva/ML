#!/bin/python
# Compare the triples - HackerRank Challange

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    result=[0,0]
    for i in range(0,3):
        if(a[i]>b[i]):
            result[0]=result[0]+1
        elif (a[i]<b[i]):
            result[1]=result[1]+1
    return result
    
            


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = solve(a, b)

    print (result)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
