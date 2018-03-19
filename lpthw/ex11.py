"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""

def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)

print fact(8)
