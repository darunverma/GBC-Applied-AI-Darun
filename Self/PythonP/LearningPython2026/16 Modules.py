# MODULE 16

# Module is a file containing a set of functions. 

import math  # Math is a module of mathematical functions.

#import maths as m # as is used to give a name, so that it could be used as m.sqrt or m.pow

#from math import sqrt # In order to import only sqrt function from math module.

def squareroot(x):
    return(math.sqrt(x)) #Calling sqrt function of module math

print(squareroot(25))

x= 59.4
print(math.ceil(x)) # Function to always print the upper value of a fraction.
print(math.floor(x)) # Function to always print the lower value of a fraction. 

a=2
b=a+2
print(math.pow(a,b)) # Function to the power value of a to the power b.

x=-10.7
y=3
print(math.ceil(x)) # always prints the upper value -10 and not -11.
print(math.fabs(x)) # return the absolute value
print(math.pow(y,2))
