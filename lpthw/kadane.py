"""                                     
                                      
Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.
 
Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.
 
Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

"""

def findMaxSum(ary):
    highSum=nextSum=0
    print ary
    print len(ary)
    print ary[0]
    for num in (0,len(ary)):
        nextSum=0
        print num
        for num1 in (num,len(ary)):
            print "Loop2"
            print num1
            print ary[num1]
            nextSum+=ary[num1]
            print nextSum
            highSum=max(highSum,nextSum)
    return highSum        

if __name__=="__main__":
    args = [1,2,3,3,3]
    maximumSum=findMaxSum(args)
    print maximumSum
