def fib(n):
    a,b =0,1
    while a<n:
        print(a)
        a,b= b,a + b
    print()
    
    # Or this

def fib2(n):
    result=[]
    a,b =0,1
    while a<n:
       result.append(a)
       a,b = b, a+b
    return result
''' You need to do
    import sys
    sys.path.append('copy full directory of module') or
    sys.path.insert(1,'copy full directory of module')
    '''

   
''' sys.path.append('directory path') is better as it 

        does not overload the standard behaviour of Python
'''

''' if you need to import two packages then use 
    /home/sam/pythonModules/module1 and /home/sam/pythonModules/module2 
    instead of doing
    sys.path.append('/home/sam/pythonModules/module1')
    sys.path.append('/home/sam/pythonModules/module2')
    because second over-writes first one
    '''


''' >>> from fibo import *
    >>>fib(500)
    It imports all the names except
     those beginning with an underscore(_).'''


''' You can even do
   >>> import fibo as FIB
   >>> FIB.fib(500)
    Or >>> from fibo import fib as fibonacci
       >>> fibonacci(50)
   the only difference
   of it being available as FIB.It's like
   changing the name while calling
    '''

if __name__ == "__main__":
     import sys
     fib(int(sys.argv[1]))


'''
    Here module can be runned even from command line
    because it executes name as main
'''

#ref: https://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script