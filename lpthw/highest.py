def sortByHeight(a):
    print a
    for i in range(len(a)-1):
        print i,a[i]
        left=a[i]
        right=a[i+1]
        if left>right:
            biggest=a[i]
            a[i]=a[i+1]
            a[i+1]=biggest
            sortByHeight(a)
    return a

if __name__=="__main__":
    print sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180])