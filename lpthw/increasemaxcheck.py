def almostIncreasingSequence(sequence):
    if len(sequence)==2:
        return sequence==sorted(list(sequence))
    else:
        for i in range(0,len(sequence)):
            newsequence=sequence[:i]+sequence[i+1:]
            if (newsequence==sorted(list(newsequence))) and len(newsequence)==len(set(newsequence)):
                return True
                break
            else:
                result=False
    return result

if __name__=="__main__":
        print almostIncreasingSequence([3,5,67,98,3])