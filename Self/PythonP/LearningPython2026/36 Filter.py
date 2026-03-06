# Filter Functions | 36

# Function which is used to perform filter operation on sequence of elements.

# Syntax of Filter Function includes : filter(argument, iterable sequence) and values from the iterable sequence is being passed to the argument, one by one. 

# Filter would return an object.

list1 = [2,3,4,5,6,7,8,9,10]

def is_even(number):
    if number%2==0:
        print(number,'Yes, number is EVEN.')
    else:
        print(number,'Number is ODD.')


is_even1 = lambda number : print("Yes, number is EVEN.") if number%2==0 else print("Number is ODD.")

is_even2 = lambda number : number%2==0

evens=tuple(filter(is_even2,list1))    
 #Instead of tuple(), I could use any sequence of elements to store the value returned (if any) from the function.

print(evens)

odds = list(filter(lambda num : num%2!=0,list1))        #It explains the power of Filter and Anonymous Functions.
print(odds)

list2 = [23,45,34,75,290,876,56,44,50]

greatfifty = list(filter(lambda num : num>50,list2))
print(greatfifty)

