""" """ """ # ARGUMENTS IN FUNCTIONS 29

# 1 DEFAULT ARGUMENTS 

def add(a,b): # Here a and b are arguments that has been passed. 
    c = a+b
    return c

a = int(input('Enter 1st value: '))
b = int(input('Enter 2nd value: '))

print('Sum of a and b: ',add(a,b))   #number of positional arguments must be same except if initialised in function.

# Example of no arguments being passed to function.

def sub(x=6,y=2):  
    return x-y

print("Subraction of X and Y is: ",sub())

# Example of overwriting the value of function variable on passing argument.

def mul(x=4,y=2):
    return x*y

print('Multiplication of X and Y is: ', mul(5))

# In order to pass multiple arguments to functions, we take help of sequence (tuple).

# 2 VARIABLE LENGTH ARGUMENTS (Adding multiple elements in an argument)

def sumofs(num1,*num2):
    print(num1)
    print(num2)
    for x in num2:
        num1=num1+x

    return num1

x=sumofs(1,2,3,4,5)   # Example of Variable Length Arguments, where the first value would be store in num1 and rest as tuple in num2.
print(x) 

# 3 KEYWORD ARGUMENTS

def person(name,age=18):
    print('Name: ',name)
    print('Age: ',age)

person(age=28,name='Darun') """

# 4 KEYWORD VARIABLE LENGTH ARGUMENT  (Adding multiple keys in an argument)

def cars(make,year,**color):
    print('MAKE: ',make,'\nYEAR: ',year)
    for n in color:
        print(n)
        for x in color[n]:
            print (x)
    return

cars(make='Honda',year=2026,color=['red','white','yellow',0], colorspecial=['silver'])


# Another Way to print dictionary items are : 


def cars2(make,year,**color):
    print('MAKE: ',make,'\nYEAR: ',year)
    for k,v in color.items():      # items is built in method for dictionary to print KEY: VALUE pair in dictionary.
        print(k,' : ',v)
    return

cars2(make='Honda',year=2026,color=['red','white','yellow',0], colorspecial=['silver'])
    