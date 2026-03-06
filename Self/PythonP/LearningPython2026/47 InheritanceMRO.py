# Inheritance and MRO | 4

# Inheritance refers to a Class belongs to Another Class.

class A:
    
    def __init__(self):
        print("Class A")

    def f1(self):
        print("Class A > F1 Works")
    
class B(A):

    def __init__(self):
        print("Class A > Class B")

    def f2(self):
        print("Class A > Class B > F2 Works")

class C(B):

    def __init__(self):
        print("Class C")

    def f3(self):
        print("Class C > F3 Works") 

class D(B,A):

    def __init__(self):
        print("Class D")

    def f4(self):
        print("Class D > F4 Works") 



obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()

obj1.f1()

#Single Level Inheritance, where Child Class would have all the values inherited from Parent Class.
obj2.f1()       
obj2.f2()

#Multi Level Inheritance, where Child Class would have all the values inherited from Parent Class(es).
obj3.f3()
obj3.f2()
obj3.f1()

# MRO = Method Resolution Order, First check its own class, Secondly checks the class mentioned first and so on..
#Multiple Inheritance, where the Child class would have all the values from multiple Parent Class(es).
obj4.f1()
obj4.f2()
obj4.f4()


