# ARRAY 27

# It is a sequence of elements with same data type unlike list, tuple, set, dictionary.


from array import *  # Array is a module in python.

arr1 = array('i',[1,3,55,77,9])  #'i' is a type code/ unicode character that defines the type of data in array

print(arr1.tolist())  # function to convert array into list.

print(len(arr1))  # function to print length of an array.

print(arr1[0])  # We could fetch array values using Index.

for x in arr1:
    print(x,end = '')

print(id(arr1)) # function to print the address of an array.

print(arr1.buffer_info())  # function to print address and length of an array.


# TEST Code

arr2 = array('f', [2.5,4.8,-3.2,6.7])

print(arr2)

for x in arr2:
    if x<0:
        continue
    print(x)