# USER INPUT | input() 18

a=5
b=6

print('Additon of value a : ',a,' and b: ',b,' is :', a+b)

# input() is an inbuilt function to take input from user.

# Way 1 to inform user that we are waiting for their input.

print('Please enter value of x: ')
x= int(input()) # to take input value as integer only because input function always returns string.
print('Please enter value of y: ')
y= float(input())

print('Addition of input value x : ',x,' and y : ',y,' is : ',x+y)

# Way 2 to inform we are waiting for their input.

x= int(input('Enter the value of X : '))
y= int(input('Enter the value of Y : '))

print('Addition of input value X : ',x,' and Y : ',y,' is : ',x+y)

x= input('Enter the value of X : ')[0] # To store only first character of user input.
y= input('Enter the value of Y : ')[0]

print(x+y)