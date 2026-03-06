# MATCH 23

# MATCH is similar to SWITCH in terms of functionalities.

num = int(input('Enter a number: '))

match num:
    case 1:                      # represents if statements
        print('One')
    case 2:
        print('Two')
    case 3:
        print('Three')
    case 4:
        print('Four')
    case 5:                      # represents elif statements
        print('Five')
    case _:                      # represents else statement
        print('Incorrect')


# TEST Code

test = 15 

match test%3:
    case 1:
        print('Remainder 1 when divided by 3')
    case 0:
        print('Number is divisible by 3')
    case _:
        print('Remainder 2 when divided by 3')
