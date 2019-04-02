def function2():
    print('a')
    function1()
    print('a2')
    print('a3')

def function1():
    print('b')
print('Before main')
if __name__=='__main__':
    function2()
    print('Inside name')
print('Outside the end of main')



