"""
A sequence of integers is called a zigzag sequence if each of its 
elements is either strictly less than all its neighbors or strictly 
greater than all its neighbors. For example, the sequence 4 2 3 1 5 3 is a zigzag, 
but 7 3 5 5 2 and 3 8 6 4 5 aren't. Sequence of length 1 is also a zigzag.

For a given array of integers return the length of its longest contiguous sub-array that is a zigzag sequence.
"""

def zigzag(a):
    print a
    print len(a)
    sequence=[]
    sequence1=[]
    if len(a)==1:
        return True
    else:
        for idx in range(0,len(a)-1):
            #print "index",idx
            if  idx%2==0:
                if a[idx]<a[idx+1]:
                    sequence.append(a[idx])
                elif a[idx]>a[idx+1]:
                    sequence1.append(a[idx+1])
            else:
                if a[idx]>a[idx+1]:
                    sequence.append(a[idx])
                elif a[idx]<a[idx+1]:
                    sequence1.append(a[idx+1])
    print sequence
    print sequence1
    return max(len(set(list(sequence))),len(set(list(sequence1))))

if __name__=="__main__":
    #print zigzag([9, 8, 8, 5, 3, 5, 3, 2, 8, 6])
    print zigzag([2, 1, 4, 4, 1, 4, 4, 1, 2, 0, 1, 0, 0, 3, 1, 3, 4, 1, 3, 4])

    #print neighbours_state(3,4,2)

