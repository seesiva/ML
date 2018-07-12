"""
https://www.hackerrank.com/challenges/30-2d-arrays/problem
"""

#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))
