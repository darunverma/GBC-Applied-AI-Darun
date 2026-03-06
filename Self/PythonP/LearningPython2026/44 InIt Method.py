# INIT Method | 44

"""

__INIT__ method is system generated method whenever a class has been created and being called everytime an object has been created.


There are two types of variables:

1. Class Variables.
These variables are defined in the class, and could be accessed by all the objects. These varibles belong to the class.

2. Instance Variables.
These variables belong to an object; hence, not every object could be able to access it.

"""

class A:
    a = 00   # Class variable, as the variable is defined in the class. 

obj1 = A()
obj2 = A()
obj3 = A()

obj1.a=11    # 'a' variable value for obj1 has been defined.
obj2.a=22    # 'a' variable value for obj2 has been defined.

print(obj1.a)   # class variable 'a' has different value for obj1
print(obj2.a)   # class variable 'a' has different value for obj2
print(obj3.a)   # class variable 'a' has global value for obj3
print(A.a)      # Global value

""" 
This defines that variable 'a' could be defined different values for different objects. 
"""


print(type(A.a))

"""----------------------"""
class B:
    def config():
        print('In configuration')
    
obj3 = B()      
obj4 = B()

obj3.a=33       # 'a' variable value for obj3 has been defined.
obj4.a=44       # 'a' variable value for obj4 has been defined.

print(obj3.a)       # Instance variable 'a' has a value for obj3.
print(obj4.a)       # Instance variable 'a' has a value for obj4.
#print(B.a)          # This would be an error, as 'a' is not class variable. It is an instance variable.

"""----------------------"""
""" There is an another way to assign class variables using INIT function """

class C:
    a=11        # global varible
    def __init__(self,a):         # Everytime an object is being created, this function has been called.
        self.a = a          # class variable

    def config(self):
        print("In config function where the class varables could be accessed as : ",self.a)


obj5=C(55)        # Object having variable values as assigned by the class variable.
obj6=C(66)        # Object having instance variable values.
obj7=C(C.a)

print(obj5.a)
print(obj6.a)  
print(obj7.a)
obj5.config()
obj6.config()
obj7.config()


"""_______________________________________"""


class family:

    family_name='Verma Family'

    def __init__(self,name,age,location,job):
        self.age = age
        self.name = name
        self.job = job
        self.location = location


    def f_name(self):
        print("Name of the family member is : ",self.name)

    def f_age(self):
        print("Age of the family member is : ",self.age)

    def f_location(self):
        print("Residence of the family member is : ",self.location)

    def f_job(self):
        print("Job of the family member is : ",self.job)


D=family('Darundeep Verma',27,'Canada','Student')
K=family('Kanika Verma',32,'Canada','CIBC Manager')
V=family('Veena Rani Verma',53,'India','Housewife')
B=family('Bachan Lal Verma',57,'India','Businessman')
P=family('Pushpa Devi',75,'India','Housewife')
N=family('Nohria Ram Verma', 83, 'India', 'Retired Government Employee')

print("Name of the Family is : ",family.family_name)
print("Member 1 :")
N.f_name() 
N.f_age()
N.f_location()
N.f_job()
print("Member 2 :")
P.f_name()
P.f_age()
P.f_location()
P.f_job()
print("Member 3 :")
B.f_name()
B.f_age()
B.f_location()
B.f_job()
print("Member 4 :")
V.f_name()
V.f_age()
V.f_location()
V.f_job()
print("Member 5 :")
K.f_name()
K.f_age()
K.f_location()
K.f_job()
print("Member 6 :")
D.f_name()
D.f_age()
D.f_location()
D.f_job()

print("\n",D.family_location,"\n",D.family_address)
