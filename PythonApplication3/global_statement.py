# ref:https://www.vskills.in/certification/tutorial/python/using-global-and-nonlocal-statement/
# ref: https://stackoverflow.com/questions/4693120/use-of-global-keyword-in-python
# ref:https://softwareengineering.stackexchange.com/questions/148108/why-is-global-state-so-evil
# ref:https://stackoverflow.com/questions/19158339/why-are-global-variables-evil/19158418#19158418
# ref:http://wiki.c2.com/?GlobalVariablesAreBad

x=50
def func(): # THis is a funtion because it independently defined (i.e not referenced to any class) 
    global x

    print('x is ', x)
    x=2
    print('Changed global x to ', x)

func()
print('Value of x is', x)

#nonlocal
def func_outer():
    x=2
    print('s is', x)

    def func_inner():
        nonlocal x
        x=5

    func_inner()
    print('Changed local x to ', x)

func_outer()


def scope_test():
    def do_local():
        spam='local spam' #this is the local variable

    def do_nonlocal():
        nonlocal spam
        spam= 'nonlocal spam' #local variable is modified using 'nonlocal' keyword

    def do_global():
        global spam
        spam ='Global spam' #global variabl is modified using global keyword

    spam= 'test spam' #this is the global variable
    do_local()
    print('After local assignment: ', spam)
    do_nonlocal()
    print('After nonlocal assigment: ',spam) #prints 'nonlocal spam' because it changes global spam not the nonlocal spam
    do_global()
    print('After global assignment: ', spam)

scope_test()
print('After global assignment: ', spam)

scope_test()
print('In global scope: ', spam)