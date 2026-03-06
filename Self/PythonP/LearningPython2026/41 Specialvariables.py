# Special Variables | 41

from ModulesandPackages.factorial import *


print('\n',globals())    #Globals is a inbuilt function to return dictionary of all Key:Value pairs of global variables in the current scope 

print("\nValue of key '__name__' is : ",__name__)


""" Now Value of key '__name__' is :  ModulesandPackages.factorial is being printed because of 

print("Value of key '__name__' is : ",__name__)  in ModulesandPackages.factorial.

In order to avoid this, I have used

if __name__ == '__main__':
    print("Value of key '__name__' is : ",__name__)  

 """





