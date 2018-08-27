def commonCharacterCount(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    x = 0
    
    for i in range(len(list1)): 
        print "i",str(i),list1[i]
        for j in range(len(list2)): 
            print "j",str(j),list2[j]
            if list1[i] == list2[j]:
                x += 1
                print "x:",str(x)
                print "List1[i]+List2[j]"+list1[i],list2[j]
                list2[j]=0
                break
    return x


if __name__=="__main__":
    print commonCharacterCount("aabcc","adcaa")