# Constructor and Types of Methods | 4546

# A Constructor is the one which would be called everytime an object has been created.

"""
There are 3 types of Methods: 

1. Instance Method  (default)
Methods that belong to the objects; It receives an Instance (object) as an implicit argument.

2. Class Method (@classmethod)
Methods that belong to the class; It receives a Class as an implicit argument. 

3. Static Method (@staticmethod)
Methods that doesn't receive anything as an implicit argument.

"""


class family:

    family_name='Verma Family'
    family_location='Chandigarh'
    family_address='Sector 37-D'

    def info(cls):                  #instance method
        return cls.family_name+' - Instance Method'
    
    @classmethod                    #this decorator would convert an instance method to class method.
    def data(cls):
        return cls.family_name+' - Class Method'

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

    @staticmethod
    def age_in_days(age):
        print(age*365.24,end='')
        return ' - Static Method'

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

print(family.family_name,' - Global Variable')       #Global variable could be accessed with the help of class name.

print(family.info(family))      #Global variable could be accessed by passing class name; however, I need to pass the class name here.

print(family.data())

print(family.age_in_days(27))


