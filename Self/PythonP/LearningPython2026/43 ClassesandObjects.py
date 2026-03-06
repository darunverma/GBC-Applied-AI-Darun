# Classes and Objects | 43

# As mentioned, I am learning about object oriented programming now, where the first class citizen is an OBJECT.

# Under Object Oriented World, everything is an object that belongs to a class.

"""
An OBJECT would have : 
A or Many Classes (defines belongingness)
A or Many Variables (defines properties)
A or Many Methods (defines behaviour)
"""

class computer:

    a = 18          # This is an object. Though, it is defined in computer class; however, it belongs to class "INT".
    print(type(a))

    def config(self):
        print("Called by the class 'Computer' object 'b'\n\nComputer Configuration is : 8GB Ram, 512GB SSD, Macbook Air 2023")


b = computer()      # This is an object. Though, it is defined outside the computer class; however, it belongs to class "Computer".
                    # Correct way of creating objects of classes.
print(type(b))

computer.config(b)         # Class calling its methods without describing a specific object.
b.config()                 # User defined object calling the user defined method from the class it belongs to.

""" Hence, computer.config(b)  ==  b.config() """

print(b.a)              # Calling variables defined in the class using class's object.

class Laptop:

    def configuration(self):
        print("Make : Apple\nModel : Macbook Air 2023\nOwner : Darundeep Verma.\n")

obj1 = Laptop()
obj2 = Laptop()

Laptop.configuration(obj1)

obj2.configuration()


