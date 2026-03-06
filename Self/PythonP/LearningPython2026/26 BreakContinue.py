# BREAK CONTINUE 26

# Q : Print the numbers NOT divisible by 3.

for x in range(10):
    if(x%3!=0):
        print(x)

# CONTINUE : Statement is used to jump to next iteration  without executing the following statements once condition has been met.
print()
for x in range(10):
    if x%3==0:
        continue
    print(x)


# Q : Print the numbers LESS THAN 5.

print()
for x in range(10):
    if x<5:
        print(x)

# BREAK : Statement is used to immediately exit from the current loop once condition has been met.
print()
for x in range(10):
    if x==5:
        break
    print(x)

    