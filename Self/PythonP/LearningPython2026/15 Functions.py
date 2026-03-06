#I am learning Python language from Telusko Youtube Chanel.I have shifted from Google Collab to VS Code to get its exposure which is imperative.

# FUNCTIONS, 15
# A block of code that runs to perform a specific task only once called. We can call the function multiple times. 

#We could either CREATE THE FUNCTIONS or use INBUILT FUNCTIONS.

print("This is Print an inbuilt Function.")

def addf():  #Created my own function using definition 'def'.
    '''Adds two values''' #Used to describe the application of the function once hovered.
    a=2
    b=3
    print(a+b)

addf()

def addf2(a,b): #User could input their own values.
    print(a+b)

addf2(4,6)

def addf3(a,b): #Function returning the output for personal use.
    return(a+b) #Return is a keyword which would return the output.

print(addf3(6,6)) #Printing the output of defined function.

