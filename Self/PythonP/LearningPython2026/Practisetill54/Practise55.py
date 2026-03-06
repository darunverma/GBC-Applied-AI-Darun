
# Since, I have completed the "PYTHON BASIC" by TELUSKO till Multithreading/ MultiProcessing. I would like to take a practise test.

# Modules | Match | Recursion | initsupermethod | Exception handling

""" Lets create a function that would check leap year """

def leapyear(year):
    match year%4:
        case 0:
            match year%100:
                case 0:
                    return f'{year} IS NOT A LEAP YEAR.'
                case _:
                    return f'{year} IS A LEAP YEAR.'
        case _:
            match year%100==0 and year%400==0:
                case True:
                    return f'{year} IS A LEAP YEAR.'
                case _:
                    return f'{year} IS NOT A LEAP YEAR.'



class h_mathematics:

    def factorial(self,number):
        if number == 1:
            return 1
        return number*self.factorial(number-1)
    
    def superpower(self):
        print('SUPER POWER EXISTS !!!')
        
class a_mathematics(h_mathematics):
    def __init__(self,number):
        self.number = number
        print('Object has been created.')
        self.result_fac = self.factorial(number)
        super().superpower()
    
    def printing(self):
        print('Factorial of ',self.number,'is : ',self.result_fac)


        





            




