# ELIF (ELSE IF) 22

x = int(input('Please enter a number between 1-5 : '))

if x==1:
    print('One')
elif x==2:
    print('Two')
elif x==3:
    print('Three')
elif x==4:
    print('Four')
elif x==5:
    print('Five')
else:
    print('Number is out of range -_-')


# TEST Code

x = int(input('Please Enter Marks (0-100) : '))

if (x>=90):
    print('Grade A+')
elif (x>=75):
    print('Grade A')
elif (x>=60):
    print('Grade B')
else:
    print('Grade C')