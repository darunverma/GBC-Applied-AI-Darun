# Abstract Class and Methods | 52

# Abstraction is hiding the complex computation from the user.

# Interface : Declaring what to do  | Implementation : Defines how to do.

# Abstract Classes and Methods; hence, are Interfaces. Till now, we have read and worked upon implementaion.

"""
IMPORTANT
1. Abstract Methods must belong to Abstract Class,
2. Abstract Methods must not be defined (implemented).
3. Abstract Classes does not have objects

from abc import ABC,abstractmethod
"""
from abc import ABC,abstractmethod


class A(ABC):               # Inherit ABC, becomes a child of abstract class.
    
    @abstractmethod
    def show(self):
        pass

    print(type(show))

#obj1 = A()
#obj1.show()

print(type(A))

"""___________________________________"""


class paymentgateways(ABC):                 # Abstract Class
    @abstractmethod
    def pay(self):                          # Abstract Method
        pass

class razorpay(paymentgateways):

    def pay(self):                                              # Abstraction enforces the creation of pay() in child classes.
        print("Payment is being made using Razorpay.")

class paytm(paymentgateways):

    def pay(self):
        print("Payment is being made using PayTM.")


""" 
In order to understand abstraction and why it is crucial, let's suppose that the above code is being handeled by third party and I am using their payment gateway in order to process the payments. Now, if they would change anything in their code, my code needs to be changed as well. In order to avoid this, I would prefer to proceed with abstraction. 
This process would make sure that certain implementations must be consistent like pay().

"""


class purchase:
    
    def __init__(self,gateway):
        self.gateway=gateway

    def checkout(self):
        print("Checking Out...")
        self.gateway.pay()

gateway1=paytm()
gateway2=razorpay()
darun=purchase(gateway2)
# darun=purchase(gateway2) # This would not work as the name of the functions are different for different payment gateways, pay() | pe()


darun.checkout()









