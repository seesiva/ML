"""
Develop a procedure which will return the sum of square of largest of 2 numbers from given 3 numbers
"""

def square(x):
    return x * x

def sumofsquare(x,y):
    return square(x)+square(y)

def sumofsquarebig2of3(x,y,z):
    big1=big2=0
    if (x>y):
       big1=x
    elif y>z:
        big2=y
    elif z>x:
        big2=z
    return sumofsquare(big1,big2)


if __name__=="__main__":
    print sumofsquarebig2of3(1,2,3)


