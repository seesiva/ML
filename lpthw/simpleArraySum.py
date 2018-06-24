#!/bin/python
#HackerRank Algorithm Challenge

from __future__ import print_function

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    i=sum=0
    while (i<len(ar)):
        sum=sum+ar[i]
        i=i+1
    return sum

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = simpleArraySum(ar)
    
    print (result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
