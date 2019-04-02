class Dog:
    kind = 'canine' # class variable shared by all instances

    def __init__(self, name):
        self.name = name # instance variable unique to each instance

d = Dog('Fido')    
e = Dog('Buddy')

print('Output of d.kind: ',d.kind) #shared by all dogs
print('Output of e.kind: ', e.kind) #shared by all dogs
print('Output of d.name: ', d.name) # Unique to d
print('OUtput of e.name: ', e.name) # Unique to e

# ref: https://docs.python.org/3/tutorial/classes.html#tut-private