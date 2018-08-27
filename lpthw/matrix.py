"""

"""
def matrixElementsSum(matrix):
    lastrow=len(matrix)-1
    totalsum=0
    print "Last Row:",str(lastrow)
    for x in matrix:
        print x
        count=0
        for y in x:
            if y==0:
                currow=matrix.index(x)
                colbelow=count
                print "Current Row:",str(currow)
                print "Current Column", str(colbelow)
                for j in range(currow,lastrow+1):
                    print "j:",str(j)
                    matrix[j][colbelow]=0
            count=count+1
            print "index:",str(count)
    print matrix
    for x in matrix:
        for y in x:
            totalsum=totalsum+y
    return totalsum
            
                
if __name__=="__main__":
    data=[[0,1,1,2],[0,5,0,0], [2,0,3,3]]
    print matrixElementsSum(data)

"""
1. Get the input matrix data
2. Passit on to matrix elements sum
3. Iterate by rows and check for unusable rows 
4. Mark them before summarizing it

"""
