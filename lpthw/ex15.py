"""
Write a program that asks the user to input 10 integers, and
then prints the largest odd number that was entered. If no odd number was
entered, it should print a message to that effect.
"""


numbers=[10,23,45,54,42,45,24,789,32,45]
largest=0
i=0
while i>len(numbers):
    print i
    if (numbers[i]%2 != 0):
        if (numbers[i]>largest) :
            largest=numbers[i]
    i=i+1


if largest >0 :
    print largest
else: 
    print "No odd numbers found!"