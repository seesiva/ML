def allLongestStrings(inputArray):
    largest=0
    coll=[]
    result=[]
    for x in inputArray:
        coll.append(len(x))
        if len(x)>largest:
            largest=len(x)
    for y in range(0,len(coll)):
        if coll[y]==largest:
            result.append(inputArray[y])
    return  result

        
if __name__=="__main__":
    data=["abc", 
 "eeee", 
 "abcd", 
 "dcd"]
    print allLongestStrings(data)

        