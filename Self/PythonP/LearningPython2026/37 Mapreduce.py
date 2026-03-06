# Map and Reduce | 37

list_= [1,2,3,4,5,6,7,8,9,10]

evens = list(filter(lambda num : num%2==0,list_))
doubles = list(filter(lambda num : num/2,evens))    
# Here num/2 would not return [1.0,2.0,3.0,4.0,5.0] rather it would return [2,4,6,8,10] because for every operation, it is returning "True" or "False" as that's what Filteration means. 
# True means number belongs to the list, False means number doesn't belong to the list. 
# Hence, If we want to perform any operation on the filtered list -> We have to use Map or Reduce.

print("Even Number : ",evens)
print("Double of Even Numbers (filter) : ",doubles)


"""-----------------------"""

# If required to perform operation on each element and retreive the output, we use : MAP

list1_ = [1,2,3,4,5,6,7,8,9,10]

doubles1 = list(map(lambda n : n*2 ,list(filter(lambda n : n%2==0, list1_))))
print("Doubles of Even Numbers (map) : ",doubles1)

"""-----------------------"""

# If required to perform a collective operation and deduce a value out of a sequence of elements (like sum of all elements in a sequence), we use REDUCE

from functools import reduce    # Reduce function belong to another module.

list2 = [1,2,3,4,5,6,7,8,9,10]
sum_ = int(reduce(lambda n,m : n+m ,list(map(lambda n : n*2,list(filter(lambda n : n%2==0,list2))))))   
#reduce function would return one value only

print(sum_)

"""-----------------------"""

list3 = [2,3,4]
sumcubes = int(reduce(lambda a,b : a+b,list(map(lambda n : n**3,list3))))
print("Sum of cubes of all the elements in the list [2,3,4] = ",sumcubes)