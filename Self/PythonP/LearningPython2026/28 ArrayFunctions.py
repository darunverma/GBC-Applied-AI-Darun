# ARRAY FUNCTIONS 28

from array import *

A = array('i',[11,22,33,44,55,66])

A.append(77) # Function to insert an(1) element at the end of an array.

print('Appended Array : ',A)

A.extend([8]) # Function to insert each element of the iterable sequence.

print('Extended Array : ',A)

A.insert(2,23) # Function to insert an element at specific index.

print('Inserted an element at 3rd Place : ', A)

A.reverse() # Function to reverse the elements of array.

print('Reversed Array : ',A) 

A2 = A  # This way we could copy arrays that would have same address, same values but different variables; hence, if we change one array, it would change another array as well.

A[2]=60

print('A: ',A,'\nA2: ',A2)

print('Address of A: ', id(A),'Address of A2: ',id(A2))

# Way to create a new array with similar values as another.

print('A: ',A)

A3 = array('i')

A3.extend(A)

print('A3: ',A3)

# Another way to create a new array with similar values as another.

print ('A: ',A)

A4 = array(A.typecode,A.tolist())  #Typecode function is used to get the data type of a variable.

print('A4: ',A4)

# Another way to create a new way with similar values as another.

print ('A: ',A)

A5 = array(A.typecode,(n for n in A)) # This is more efficient way in terms of memory management.

print('A5: ', A5)


# TEST Code


X = int(input('Be a part of ARRAY creation, please tell how many numbers you would like to enter: '))

Arr = array('i',(n for n in range(X)))
print('Array values before insertion: ',Arr)

for n in range(X):
    Arr[n] = int(input('Please enter the number: '))

print('Array values after insertion: ',Arr)


# TEST Code another way

X = int(input('Be a part of ARRAY creation, please tell how many numbers you would like to enter: '))

Arr2 = array('i',[])

print('Array values before insertion: ',Arr2)

for n in range(X):
    Arr2.append(int(input('Please enter the number: ')))

print('Array values after insertion: ',Arr2)
