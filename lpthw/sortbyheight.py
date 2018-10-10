def sortByHeight(a):
    l = sorted([i for i in a if i > 0])
    print l
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l

if __name__=="__main__":
    print sortByHeight([-1,-1,3,4,10,2,-1,200,4,2])