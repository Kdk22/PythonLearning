class MyClass():
    i=12345

    def f(self):
        return 'Hello World'
     #@staticmethod is used if self is not defined inside function
    #https://stackoverflow.com/questions/37638739/python-class-and-method-instantiation
    @staticmethod
    def g():
        return 'It\'s wonderful.'
    def h(self,size):
        self.size= size
        return self.size
        
# Example of attribute references
x= MyClass()
print(x.i)
print(x.g())
print(x.f())


print(MyClass.i)
print(MyClass.f('string'))
#print(MyClass.f()) # This gives error:- TypeError: f() missing 1 required positional argument: 'self'
'''
THis is because it's not bound to any instance of MyClass.And method 'f(self)'
wants instance as it's first argument.
Here is the link for more
https://julien.danjou.info/guide-python-static-class-abstract-methods/
So you can do the following
'''
print(MyClass.f(MyClass())) #THis prints Hello World
#Or
print(MyClass().f) #now method is bound to class
#print(MyClass().f(6))



