# Method Overwriting | 51

# Method Overwriting is a process of updating the functionality of the pre defined methods as per usage.

class methodoverwriting:

        def __init__(self,cash):
            self.cash = cash
        def __add__(self,operand):
            return f'Combined Cash : {self.cash + operand.cash}'
        def __gt__(self,operand):
            if self.cash > operand.cash:
                return True
            else:
                return False
        __str__ = lambda self : f'Cash : {self.cash}'
        __pow__ = lambda self,operand : self.cash**operand.cash

"""  def __str__(self):
        return f'Cash : {self.cash}'
def __pow__(self,operand):
    return self.cash**operand.cash """

darun = methodoverwriting(10)
kanika = methodoverwriting(20)

print(darun.__str__())
print(kanika)

combined = darun+kanika
print(combined)

if darun > kanika:
     print("Darun has more money.")
else:
     print("Kanika has more money.")

print(darun**kanika)




                