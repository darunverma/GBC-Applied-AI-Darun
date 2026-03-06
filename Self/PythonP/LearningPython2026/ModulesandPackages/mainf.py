# This is the main function.

import factorial        # Module has been imported so that its functions could be accessed.

x= int(input("Enter the number to find factorial for : "))

result=factorial.fact(x)

print(result)


print("Value of key '__name__' is : ",__name__)