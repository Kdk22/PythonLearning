class Dog:
    tricks =[] #mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_tricks(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e  = Dog('Buddy')
d.add_tricks('roll over')
e.add_tricks('Play dead')
print(d.tricks) #unexpectedly shared by all dogs

    # Correct  design is to use an instance variable
class Dog:
        def __init__(self, name):
            self.name = name # these are the data attributes
            self.tricks =[] # creates a new empty list for each dog


        def add_tricks(self, trick):
            self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_tricks('roll over')
e.add_tricks('play dead')
print('D.tricks :',d.tricks)
print('E.tricks: ', e.tricks)

#ref: https://docs.python.org/3/tutorial/classes.html#tut-private

# My trial
''' 
    What if we don't pass self inside method add_tricks 
'''
print('-'*20, 'Without Passing Self in Methods','-'*20)
class Dog:
    tricks =[]
    def __init__(self, name):
        self.name = name
    def add_trick( trick):
        # tricks.append(trick)   #I tried this but it cannot identify tricks
        Dog.tricks.append(trick)

d= Dog('Fido')
e =Dog('Buddy')
Dog.add_trick('Bark') # method accessed through class name 
# e.add_trick('Mark') # method cannot be accessed from object reference
'''
    Now we cannot access the add_trick method using the instance or object
    of class. It can be accessed only through the class name
'''
print(Dog.tricks)
''' This means data attributes may be referenced by methods as 
    well as by ordinary users ('clients') of an object.
'''


