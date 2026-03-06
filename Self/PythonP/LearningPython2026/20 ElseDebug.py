# ELSE & DEBUGGING 20

a=7

if (a%2==0):     # If block would only execute if a is Even number
     print('Even')
else:
    print('Odd')

# Errors could be of two type : Logical Error and Syntax Error. These days IDEs are smart enough to point Syntax Errors; however, Logical Errors are difficult to find. 
# Errors are called Bugs; hence, process of finding and removing bugs is Debugging.

# Breakpoints: If I want my code to execute upto specific line, I could add breakpoints. this would help me to control the flow and check the code behaviour line by line.

# TEST Code

num = int(input('Enter a number: '))

if num>0:
     print('Positive Number')
elif num<0:
     print('Negative Number')
else:
     print('Zero')



     