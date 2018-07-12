
"""
The first line contains a single positive integer  denoting the number of the known digits.
The second line contains the list of single-space separated known digits.
It is guaranteed that the answer exists and it is unique.
"""
def fillZerotoArray(arr,totaldigits):
    for i in range(1,totaldigits,2):
        arr.insert(i,0)
    return arr

if __name__ == '__main__':
    arr = []
    n=raw_input() # single positive integer denoting the number of the known digits
    arr = map(int, raw_input().rstrip().split())
    print len(arr)
    # Logic to determine the number of digits to fill
    num_of_digits_to_fill=len(arr)+(len(arr)-1)
    print "Digits to fill: " + str(len(arr)-1)
    print "Length of the answer for square: " + str(num_of_digits_to_fill)
    print fillZerotoArray(arr,num_of_digits_to_fill)