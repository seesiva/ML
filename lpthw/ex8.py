"""
Higher Order Functions:
HoF: Handling function as arugments
"""
def summation(nums):
    return sum(nums)

def main(f, *args):
    result = f(*args)
    print (result)

if __name__=="__main__":
    main(summation, [1,2,3,4]) # output 10