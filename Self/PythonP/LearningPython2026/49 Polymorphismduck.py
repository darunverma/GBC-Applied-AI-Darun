# Polymorphism and Duck Typing | 49


# Meaning of polymorphism is that ONE ELEMENT would have MULTIPLE FORMS.

class dog:
    def sound(self):
        print('Dog Barks')

class cat:
    def sound(self):
        print('Cat Meows')

class duck:
    def says(self):
        print('Duck Quacks')

class trainer():
    def code(self, animal : dog):          
        # In this way, I could pass objects of other classes. This doesn't mean that the object I am passing belongs to dog class.
        
        animal.sound()
        print('Trainer Reacts')


spiky = dog()
katy = cat()
mamba = duck()

t1 = trainer()
t1.code(spiky)      # It would take 'Spiky' as an object of dog() class and produce output if sound method exist in the class.
t1.code(katy)       # It would take 'Katy' as an object of class() class and produce output if sound method exist in the class.
t1.code(mamba)      # It would take 'Mamba' as an object of duck() class and produce output if sound method exist in the class.


""". THIS MEANS THAT A CLASS METHOD WOULD ONLY BE INHERITED IF METHOD EXISTS, IRRESPECTIVE OF WHAT CLASS WE HAVE MENTIONED WHILE RCV OBJECT AS ARGUMENT . """
""". THIS MEANS THE BIRD WOULD BE DUCK IF IT QUACKS . """








