"""
Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).
Note:  is considered to be an even index.
"""
import sys

if __name__=="__main__":
    string_list=[]
    T=int(raw_input())
    for i in range (0,T):
        inputstring=raw_input()
        string_list.append(inputstring)
    for i in range (0,T):
        even=""
        odd=""
        #print i
        #print string_list[i]
        for j, char in enumerate(string_list[i]):
            print j
            if  j % 2 == 0:
                #print char
                even=even+char
            else:
                #print char
                odd=odd+char
        print even, odd