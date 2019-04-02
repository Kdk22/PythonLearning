class Myclass:
    def mypublicmethod(self):
        print('Public Method')
    def __myprivatemethod(self):
        print('Private Method')

obj = Myclass()
obj.mypublicmethod()

# obj.__myprivatemethod() # try to run this

print(dir(obj))

obj._Myclass__myprivatemethod()

class Foo:
    def __init__(self):
        self.__baz =42

    def foo(self):
        print(self.__baz)

class Bar(Foo):
    def __init__(self):
        super().__init__()
        self.__baz = 21

    def bar(self):
        print(self.__baz)

x = Bar()
x.foo()
x.bar()
print(x.__dict__)

'''

# THis code is from python documentation but I don't understood
so below is the simiar code to this from stack
    class Mapping:
        def __init__(self, iterable):
            self.items_list =[]
            self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update

    class MappingSubclass(Mapping):

    def update(self, keys, values):
    for item in zip(keys, values):
    self.items_list.append(item)
'''
# ref : https://stackoverflow.com/questions/1162234/what-is-the-benefit-of-private-name-mangling-in-python

class Parent:

    def __init__(self):
        self.__help('will take child to school')
    def help(self, activities):
        print('parent', activities)

    __help = help #private copy of orginal help() method

class Child(Parent):
    #new signature for help() and does not break __init__()
    def help(self, activities, days):
        self.activities = activities
        self.days = days
        print('Child will do ', self.activities, self.days)



print('list parents & child responsibiliteis')
c = Child()
c.help('laundry', 'Saturdays')

#ref : https://stackoverflow.com/questions/38606804/private-variables-and-class-local-references?rq=1

class Foo:
    __attr = 5
    attr= 6
    print(__attr) #prints 5
    #exec('print(__attr)') #raises NameError
    exec('print(attr)') #prints 6
    exec('print(_Foo__attr)') #prints 5
    #compare above two exec() methods
    '''
       Notice that code passed to exec, 
       eval() or execfile() does not consider
       the classname of the invoking class to
       be the current class; 
    '''
print(Foo.attr) 
#print(Foo.__attr) #raises AttributeError
#print(_Foo__attr) #error
c = Foo()
print(c._Foo__attr) #prints 5
'''Outside of class private varibles or dunders variables
    can be called through object._Classname__attributename