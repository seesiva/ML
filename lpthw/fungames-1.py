#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the funGame function below.
#
def funGame(a, b):
    #
    # Write your code here.
    #

if __name__=="__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())
    
        a = map(int, raw_input().rstrip().split())

        b = map(int, raw_input().rstrip().split())

        result = funGame(a, b)

    fptr.close()