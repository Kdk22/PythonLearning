'''
    Function can be defined outside the class 
    and even function object can be assigned to a
    local variable in the class.
'''
def f1(self, x, y): #defining function outside of the class
    return min(x, x+y) 

class C:
    f = f1 #Creating object of function or you can say assigning function to local variable

    def g(self):
        return 'Hello world'
    h= g #Creating object of function or you can say assigning function to local variable
    #print(f(C,10,20))

c = C()
print(f1(c,5, 10)) #Here we have passed class instance
print(c.h())
print(c.f(5,10)) #accessing function via local variable,here we are not passing class instance
''''
    Here f, g, h are all attributes of class C that 
    refer to function objects, and consequently they are all
    methods of instances of C. h is equal to g
'''
# ref: https://docs.python.org/3/tutorial/classes.html#tut-private

# Check this out
'''
    What happens if we remove the self in a function parameter
    that is inside a class
'''
class C:
    def g():
        return 'Hello world'

c = C()
# print(c.g()) #TypeError: g() takes 0 positional arguments but 1 was given
print(C.g()) #'Hello World'
'''
    Now defining a function outside the class
    and assigning function to local variable i.e
    using function object that is also a class attribute
    to access a function outside of class.
'''
def f1():
    return 'Hello World without self'

class C:
    f = f1

    def g():
        return 'Hello Universe'
           
c =C()
# print(c.f())
print(C.f())

'''
    Methods may call another methods by using methods
    attributes of the self argument
'''
class Bag:
    def __init__(self):
        self.data =[]
    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

b= Bag()
b.addtwice('Letrio')
print(b.data)

b.add('Woven')
print(b.data)

c = Bag()
c.add('WSDO')
print(c.data)