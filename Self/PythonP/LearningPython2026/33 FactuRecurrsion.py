# FACTORIAL of a number with recursion

result=1
def rfact(X):
#    global result.  # OR I could directly change value of result by specifying as global result.
    globals()['result']=globals()['result']*X  
    if X==1:
            return result
    rfact(X-1)
  
rfact(int(input('Please enter a number: ')))

print(result) 

result = 1

def fr(X):
    global result
    result= X*result  
    if X>1:
        fr(X-1)
    else:
        return(result)
      
X= int(input('Please enter a number : '))
fr(X)
print(result)

# Another Beautiful Way 

def fr2(X):
    
    if X==1:
        return 1
    
    return X*fr2(X-1)                      # This shows that we could also use functions as loops with recursion.

X= int(input('Please enter a number : '))
R=fr2(X)
print(R)

""" def recursivesum(X,i):

    if X[i]==len(X):
        return X[i]
    return X[i]+recursivesum(X,i+1)

i=0
X=range(1,11)
Y = recursivesum(X,i)
print(Y) """