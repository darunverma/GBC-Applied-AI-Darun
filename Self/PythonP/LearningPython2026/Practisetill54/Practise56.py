# Since, I have completed the "PYTHON BASIC" by TELUSKO till Multithreading/ MultiProcessing. I would like to take a practise test.

"""Because it isn't possible to import the package/ module that has spaces in name; hence, a new package has been created."""

import Practise55

try : 
    year = int(input("Enter A YEAR : "))
    result = Practise55.leapyear(year)
    print(result)

    number = int(input("ENTER A NUMBER : "))
    darun_user=Practise55.a_mathematics(number)
    darun_user.printing()

except ValueError:
    print('Year and Number could only be a positive integer.')

except Exception:
    print('Unknown error occured.')

finally:
    print('CODE EXECUTION COMPLETED')










