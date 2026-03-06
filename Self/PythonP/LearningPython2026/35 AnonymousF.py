# Anonymous Functions | 35

# Anonymous Functions are the ones that doesn't have name and could be represented with Lambda.

# Reason for the introduction is because there could be some small operations which doesn't require a function to be defined to avoid space allocation.

# Syntax of Anonymous Functions is "Name of the function = Lambda Arguments : Operation"


"""def even_odd_(operation):
    High Order Function
    list1_ = list()
    list1_ = operation()    #operation() = input_()
    for i in list1_:
        if i%2==0:
            print(i,"is EVEN number.")
        else:
            print(i,"is ODD number.")

    return None

def input_():
    list1_ = list()
    x = int(input("EVEN OR ODD\nKindly enter, How many numbers you would like to check: "))
    for i in range(x):
       y= int(input("Enter the number : "))
       list1_.append(y)

    return list1_

even_odd_(input_) """

even_odd_anon = lambda num : print("EVEN") if (num%2==0) else print("ODD")
even_odd_anon(24)