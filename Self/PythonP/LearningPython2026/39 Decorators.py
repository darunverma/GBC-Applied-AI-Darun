# Decorators | 39

# Decorator is like a wrapper.

""" def greater(func):  #greater function is decorator.

    def wrap(a,b):
        if a<b:
            a,b=b,a

        return func(a,b)

    return wrap     #inner function is being called


@greater            #decorator is used to take divide function as an argument
def divide(a,b):
    return a/b

@greater
def diff(a,b):
    return a-b


print(divide(2,4))
print(diff(2,4)) """


""" def log(func):

    def wrap(a,b):
        print('Values are ',a," ",b)
        result= func(a,b)
        print(result)
        return None

    return wrap



def is_even(funct):

    def wrap(a,b):
        if a%2==0:
            return funct(a,b)
        else:
            return 'Number is odd'
    return wrap 

@is_even
@log
def power(a,b):
    return a**b

print(power(2,4))


# Values are 2 4
# 16
# None """


def logger(func):
    print("Before function runs.")

    def wrap():

        return func()

    return wrap

@logger
def greet():
    print ('Hello Python')
    return "After function runs."

print(greet())