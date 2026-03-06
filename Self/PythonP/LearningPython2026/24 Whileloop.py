# WHILE LOOP 24

# LOOPS : To run a block of code multiple times until a condition is fulfilled. 

x=4
i=0

while i<x:
    print(x)
    i +=1     # increment of value i by 1


# Nested Loops as just like Nested If, we could use the same here as well.

i=1
while i==1:
    print('Darun ',end='')          #By default, print function would end with \n; however, we could change it by specifying.
    while i<=10:
        print('Rocks ! ',end='')    #Specify end
        i +=1

# Test Code

i=1
print()
while i<=10:
    if i%2==0:
        print(i)
    i +=1