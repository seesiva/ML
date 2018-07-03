#!/bin/python

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    sumd1=sumd2=0
    print len(arr)
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            #print (arr[i][j])
            if(i==j):
                sumd1=sumd1+arr[i][j]
            if (i+j==len(arr)-1):
                sumd2=sumd2+arr[i][j]
    return abs(sumd1-sumd2)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    print (result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
