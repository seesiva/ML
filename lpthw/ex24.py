""" 
Given a base- integer, , convert it to binary (base-). 
Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.
"""
#!/bin/python

import math
import os
import random
import re
import sys

def getMaxnumberofConsecutiveOnes(n):
    ans=0
    while n>0 :
        n &= (n<<1) # Clears the least significant bit by moving one bit to the left
        ans += 1
    return ans

if __name__ == '__main__':
    n = int(raw_input())
    print getMaxnumberofConsecutiveOnes(n)


"""
Additional notes
---------------- 
* For input value n=27 what will happen ?
* convert the number 27 to binary using bin (27) and follow the steps as provided below
* Refer the Brian Kernighan's way works

27	                0	0	0	1	1	0	1	1	    27
27 <<               1	0	0	1	1	0	1	1		54
AND (27, 27 << 1)   0	0	0	1	0	0	1	0	    18 (row1 * row2 bit to bit multiply)
18 << 1	            0	0	1	0	0	1	0	0	    36
AND (18, 18 << 1)	0	0	0	0	0	0	0	0	    0   (row3 * row4 bit to bit multiply)
