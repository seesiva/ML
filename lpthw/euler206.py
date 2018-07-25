
"""
The first line contains a single positive integer  denoting the number of the known digits.
The second line contains the list of single-space separated known digits.
It is guaranteed that the answer exists and it is unique.
"""
import math as Math

def fillZerotoArray(arr,totaldigits):
    for i in range(1,totaldigits,2):
        arr.insert(i,0)
    return arr

def is_square(n):
    return n**0.5 == int(n**0.5)


if __name__ == '__main__':
    arr = []
    n=raw_input() # single positive integer denoting the number of the known digits
    arr = map(int, raw_input().rstrip().split())
    print len(arr)
    # Logic to determine the number of digits to fill
    num_of_digits_to_fill=len(arr)+(len(arr)-1)
    print "Digits to fill: " + str(len(arr)-1)
    print "Length of the answer for square: " + str(num_of_digits_to_fill)
    #print fillZerotoArray(arr,num_of_digits_to_fill)
    zerofillednumber = '0'.join(map(str, arr))
    data= long(zerofillednumber)
    print data
    while (data > 0):
        digit = data % 10
        print digit
        data = data / 10
