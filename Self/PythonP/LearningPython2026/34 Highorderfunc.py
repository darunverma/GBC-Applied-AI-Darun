# Higherorder Functions 34

# When a function would be passed to a function as an argument, it is called higher order function.

# This defines that python is a high level functional programming language where "Functions" become the first class citizens. s


x,y=0,0

def take_input():  
      
    global x,y

    x=int(input("Enter the value of 1st integer: "))
    y=int(input("Enter the value of 2nd integer: "))

    return None

def addition(high_order_function):          #addition() is a high order function because it is accepting a function as an argument
    """High Order Function"""
    high_order_function()           # take_input() 
    print("Sum of 1st integer ",x," and 2nd integer ",y,"is ",x+y)

    return None



#addition(take_input)      #A function has been called : addition(), A function has been passed as an argument : take_input

def square(n,operation):
    list_1 = list()
    list_1 = operation(n)

    for i in list_1:
        print(i**2)
    return None

def input_n(n):
    list_1 = list()
    for i in range(n):
        x=int(input("Enter a number : "))
        list_1.append(x)

    return list_1


square(5,input_n)


