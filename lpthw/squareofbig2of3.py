"""
Develop a procedure which will return the sum of square of largest of 2 numbers from given 3 numbers
"""
import unittest

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


class MyTests(unittest.TestCase):
    def test_Square(self):
        self.assertEqual(square(2),4)
    
    def test_SumofSquare(self):
        self.assertEqual(sumofsquare(2,2),8)
    
    def test_SumofSquareNegative(self):
        self.assertEqual(sumofsquare(-1,-1),2)

    def test_SumofSquareof2ofBigof3(self):
        self.assertEqual(sumofsquarebig2of3(1,2,3),13)

if __name__=="__main__":
    unittest.main()
    print sumofsquarebig2of3(1,2,3)
