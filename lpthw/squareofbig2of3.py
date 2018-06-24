"""
Develop a procedure which will return the sum of square of largest of 2 numbers from given 3 numbers
"""
import unittest

def square(x):
    return x * x

def sumofsquare(x,y):
    return square(x)+square(y)

def sumofsquarebig2of3(x,y,z):
    result=0
    if (x>=z) and (y>=z):
       result=sumofsquare(x,y)
    elif (y>=x) and (z>=x):
         result=sumofsquare(y,z)
    elif (x>=y) and (z>=y):
         result=sumofsquare(x,z)
    return result


class MyTests(unittest.TestCase):
    def test_Square(self):
        self.assertEqual(square(2),4)
    
    def test_SumofSquare(self):
        self.assertEqual(sumofsquare(2,2),8)
    
    def test_SumofSquareNegative(self):
        self.assertEqual(sumofsquare(-1,-1),2)

    def test_SumofSquareof2ofBigof3WhenAllEqual(self):
        self.assertEqual(sumofsquarebig2of3(1,1,1),2)

    def test_SumofSquareof2ofBigof3WhenTwoEqualScenario(self):
        self.assertEqual(sumofsquarebig2of3(1,5,1),26)

    def test_SumofSquareof2ofBigof3WhenXYGreaterScenario(self):
        self.assertEqual(sumofsquarebig2of3(2,5,1),29)

    def test_SumofSquareof2ofBigof3WhenYZGreaterScenario(self):
        self.assertEqual(sumofsquarebig2of3(1,3,2),13)

    def test_SumofSquareof2ofBigof3WhenXZGreaterScenario(self):
        self.assertEqual(sumofsquarebig2of3(3,2,3),18)

    def test_SumofSquareof2ofBigof3WhenXZNegativeScenario(self):
        self.assertEqual(sumofsquarebig2of3(-1,-2,3),10)

if __name__=="__main__":
    unittest.main(exit=False) #Added exit=False to continue after completing the unit tests
    print sumofsquarebig2of3(1,2,3)
