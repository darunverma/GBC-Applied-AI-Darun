# Modules and Packages | 40

# This is the main function that defines how we could import packages.

from ModulesandPackages.factorial import *       # Package has been imported so that its functions could be accessed.

x= int(input("Enter the number to find factorial for : "))

result=fact(x)

print(result)
