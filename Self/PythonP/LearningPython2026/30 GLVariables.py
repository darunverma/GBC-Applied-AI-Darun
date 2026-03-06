# GLOABAL & LOCAL VARIABLES 30

# GLOBAL Variables : Defined outside of all the functions and could be accessed by anyone.

# LOCAL Variables : Defined inside the function and could be accessed only by that function.


""" a=10 # Global

def lvariable(a=20): #Local
    print(a)

lvariable()
print(a) """

# GLOABLS() function is used to use global variables inside the function even if same variable is defined inside that same function.

b=30

def lvariable(b=40):
    c=globals()              # I could write it as globals()['b']
    print('Global value of b: ',c.get('b'))
    print('Local value of b: ',b)
    globals()['b'] = 50

lvariable()
print('Updated global value of b: ',b)