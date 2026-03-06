# Init and Super Method with Inheritance | 48

# Since we are studying about python being an Object Oriented Programming Language. A defined class is actually a child class that inherits another predefined class "OBJECT".


class A(object):            # Here, OBJECT is a predefined class.

    def __init__(self):
        print('In INIT Method A')

    def f1(self):
        print('F1 Works')

"""
Parent Class = Base Class    = Super Class
Child Class  = Derived Class = Sub Class

Hence, super() method could be used in order to call parent class.
"""





class B(A):            # Here, OBJECT is a predefined class.

    def __init__(self):
        super().__init__()
        print('In INIT Method B')

    def f2(self):
        super().f1()
        self.f1()
        print('F2 Works')


obj1 = B()              # INIT Method is being checked first in own class and if no method is found then being checked in the parent (inherited) class.

obj1.f2()