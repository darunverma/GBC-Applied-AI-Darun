# RECURSION 31

# Recursion is a technique where the function would call itself  to solve a problem.

# Default limit of a recursion is by default 1000 using  import sys and sys.setrecursionlimit(10)

# sleep(x) is a function if I would like to slow down the execution of the code by x seconds.

# globals() is a function we use that helps us to use global variables inside a function; however, we would not be able to update its values inside the function, we could only fetch and use the values.
# Hence, in order to update it we must specifiy the variable X with 

 # TEST Code

""" y=1

def test2(x):
    global y
    print(x-(x-y))
    y+=1
    if y<=x:
        test2(x)


def test1(x):
    print(x)
    if x>1:
        test1(x-1) """

c=1

def test3(x):
    global c
    print('Factorial of X where X is ',x,' is = ',x,' multiplied by ',x-1,'!')
    c=c*x
    if x>1:
        return x*test3(x-1)

    return c

X=int(input('Please enter a number: '))
test3(X)
print(c)

#test2(X)

