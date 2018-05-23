"""
Given an integer, , print its first  multiples. Each multiple  (where ) should be printed on a new line in the form: n x i = result.
"""

#!/bin/python

import sys



if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,11): 
        print "%d x %d = %d" % (n,i, (i*n))
