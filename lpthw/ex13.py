"""
Python closures
A closure is a way of keeping alive a variable even when the function has returned.
So, in a closure, a function is defined along with the environment. 
In Python, this is done by nesting a function inside the encapsulating function and
then returning the underlying function.
"""

def add_5():
    five =5

    def add(arg):  ##Nested function
        return arg+five
    
    return add

if __name__ == "__main__":
    closure1 = add_5()
    print (closure1(2))
    print (closure1(2))