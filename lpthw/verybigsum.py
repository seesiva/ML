#!/bin/python

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    i=sum=0
    while (i<len(ar)):
        sum=sum+ar[i]
        i=i+1
    return sum

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(long, raw_input().rstrip().split())

    result = aVeryBigSum(ar)
    print (result)

    #fptr.write(str(result) + '\n')

    #fptr.close()