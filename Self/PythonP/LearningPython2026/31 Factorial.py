# FACTORIAL 31


def fact(x):
    
    i=1
    result=1
    while i<=x:
        result = result*i
        i +=1
    return result

X= int(input('Please enter a number 1-9: '))
R= fact(X)
print(R)


# pass is used as placeholder for future code; hence, once defined it would avoid the errors.

# Another Way


def fact2(x):
    res=1
    for n in range(1,x+1):
        res =n*res
    return res


Num=int(input('Please enter a number: '))
print('Factorial of ', Num, ' is : ', fact2(Num))





# TEST Code

def fact(n):
    result =1
    for n in range(1,n+1):
        result = result * n
    return result 

res=fact(0)
print(res)