# OPERATOR OVERLOADING | 50 

# This concept defines that an operator could act differently if it is overwritten.


a = 5
b = 6
d = a+b

c = int.__add__(a,b)
if d==c:
    print('D and C are EQUAL')

e = a.__add__(b)
print(e)


"""_____________________________________________________"""

class family:

    family_name='Verma Family'

    def __init__(self,name,age,location,job):        # Method Overwriting
        self.age = age
        self.name = name
        self.job = job
        self.location = location

    def __add__(self, operand):                     # Method Overwriting
        return f'Combined : {self.age + operand.age}'

    def __gt__(self,operand):                       
        # Method Overwriting, means every function/ method could be overwritten; however, I need to understand/know that an operator would call by default which method so that I could overwrite its functionality. 
        if self.age > operand.age:
            return True
        else: 
            return False


    """ def f_name(self):
        print("Name of the family member is : ",self.name)

    def f_age(self):
        print("Age of the family member is : ",self.age)

    def f_location(self):
        print("Residence of the family member is : ",self.location)

    def f_job(self):
        print("Job of the family member is : ",self.job) """
    
    def __str__(self):                                                 
         # METHOD OVERWRITING as __str__ is a pre defined function in "Object" class.

        return f"Name of the family member is : {self.name} \nAge of the family member is : {self.age} \nResidence of the family member is : {self.location} \nJob of the family member is : {self.job}"       
    
    # In case, if I would like to return the string in specfic format.



D=family('Darundeep Verma',27,'Canada','Student')                           # Using __init__ method which is bring overwritten
K=family('Kanika Verma',32,'Canada','CIBC Manager')
V=family('Veena Rani Verma',53,'India','Housewife')
B=family('Bachan Lal Verma',57,'India','Businessman')
P=family('Pushpa Devi',75,'India','Housewife')
N=family('Nohria Ram Verma', 83, 'India', 'Retired Government Employee')

print("Name of the Family is : ",family.family_name)


""" print("Member 1 :")
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
D.f_job() """


print('Member 1 :\n',N.__str__())       # Using __str__ method which is bring overwritten
print('\nMember 2 :\n',P)
print('\nMember 3 :\n',B)
print('\nMember 4 :\n',V)
print('\nMember 5 :\n',K)
print('\nMember 6 :\n',D)


combined = N.__add__(P)                # Using __add__ method which is bring overwritten

print(type(combined))
print(combined)


if D > P:                              # Using __gt__ method which is bring overwritten
    print('N is older')
else:
    print('P is older')


