# Inner Function | 38

from functools import reduce


def sums():                 # Outer Function
          # Inner Function : Defining inside a function

    def take_input():
        """Inner Function : Could only be called inside this sums function."""
        list1 = list()
        i=1

        X = int(input("SUM OF LIST\n Please enter how many number you would like to enter in the list : "))
        while i<=X:
            userinput = int(input("Please enter the number : "))
            list1.append(userinput)
            i+=1

        return list1

    list1 = take_input()
    lsum = reduce(lambda a,b : a+b, list1)

    return lsum

X = sums()
print(X)

# take_input() Could not be called 

"""-----------------------------------"""

def outer():
    print('Outer Function')
    def inner():
        print('Inner Function')
    return inner
    


outer()

#inner()     #Would not be able to call this function as it is out of scope.

#In case if I want to call inner function from outside then I have to return the inner function and assign it in outer scope. 

outerscope = outer()
outerscope()
    



