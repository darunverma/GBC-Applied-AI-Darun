# FOR Loop 25
print("While Loop")

List = [1,10,'Darun','Jewellery',100,35.6]
length = len(List)
i=0

while i<length:
    print(List[i])
    i+=1

# Now I could also use For Loop here which fetch the value 1 by 1.
# FOR Loop only works with sequences.

print('For Loop')

for value in List:
    print(value)


# TEST Code

for v in range(10):
    print(v, end='')


