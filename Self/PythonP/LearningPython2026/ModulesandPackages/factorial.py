# This python file has been created in order to describe the functioning of Python Modules and Packages.

# Package is a Folder, for example "40 Modpack"
# Module is a python file containing functions and operations except main function.

def fact(X):
    if X==0:
        return 1
    
    return X*fact(X-1)

# This function has been created, that would take the input value X as an argument and returns factorial.

if __name__ == '__main__':
    print("Value of key '__name__' is : ",__name__)     

#  When called in "Special Variables | 41", this statement would return ModulesandPackages.factorial; however, if this operation is independently run in this file, it would return __main__ because then it would run as a main file.