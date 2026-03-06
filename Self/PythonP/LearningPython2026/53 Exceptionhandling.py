# Exception handling | 53 

# Possibilities of crash/ errors in softwares must be handeled. 

"""
Types of errors : 

1. Compile Time Error.
Handeled by the compiler itself, easiest to figure.

2. Logical Error.
Predicted output is not equals to the expected output, handeled by the software testers.

3. Runtime Error (Exception).
Must be handled by the developer considering all the exceptions and cases. 
"""

print('Resource opened successfully.')      # Ways to do coding.


#a = 5
#b = 0               # Exception needs to be handeled.

"""
In order to handle exceptions, I should figure out :
Critical Statements and Normal Statements


Every type of exceptions is mentioned in : Exception Hierarchy of Python

"""

try:
    #result = a/b
    #print('Result is : ',result)
    a = int(input('Enter Numerator : '))
    b = int(input('Enter Denominator : '))

    result = a/b
    print('Result is : ',result)

except ZeroDivisionError as zd:                           
    print('Division by 0 is not allowed.', zd)
except ValueError as ve:
    print('Values must be integers.', ve)
except Exception as e:
    print('Error Occured', e)

finally:                            # Would always execute
    print('Resource closed finally.')

# Try block must need either finally block or except block.

# Multiple Exceptions block to handle different types of exceptions. 
"""
try and except block has been used in order to handle execptions which works similar to if and else, which means :

'try' block would execute first; however, if it would raise any exceptions the 'except' would execute.
"""












