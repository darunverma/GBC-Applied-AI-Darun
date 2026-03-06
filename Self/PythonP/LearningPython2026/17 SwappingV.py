# SWAPPING OF VARIABLES 17

#Way 1

a=5
b=6
print('Before Swapping \na =',a,', b =',b)

c = None # Create a variable without assigning any value using None.
c=b
b=a
a=c

print('After Swapping \na =',a,', b =',b)

#Way 2
a=5
b=6
print('Before Swapping \na =',a,', b =',b)

a=a+b
b=a-b
a=a-b

print('After Swapping \na =',a,', b =',b)


#Way 3 
a=5
b=6
print('Before Swapping \na =',a,', b =',b)
a,b=b,a #Python way of swapping two variable. That's why its a KING.
print('After Swapping \na =',a,', b =',b)

# This process of swapping variables in pythonic way called : Tuple Packing and Tuple Unpacking where "b,a" values are packed in a Tuple so that it could be assigned upon unpacking to "a,b" in a single line.

str1 = 'Darun'
str2 = 'Verma'
print('Before Swapping \nFirst Name =',str1,', Last Name =',str2)

str1,str2=str2,str1
print('After Swapping \nFirst Name =',str1,', Last Name =',str2)

