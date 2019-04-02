# ref: https://docs.python.org/3/tutorial/errors.html
while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError:
        print('Ooops ! THat was no valid number. Try agian..')
     
    '''   If the error type matches then only in displays message.
        If the error type is not matched then it is passed to outer
        try statements, if no handler is found to handle that
        statement then it is unhandled exception and execution
        stops 
        '''
        
'''  Therefore you can add more than one except clause in try statement
            except (RuntimeError , TypeError, NameError):
            pass
        '''

# I didn't understood this
class B(Exception):
    print('It\'s B')
    pass

class C(B):
    print('It\'s C that extracts B')
    pass

class D(C):
    print('It\'s D that extracts C')
    pass
for cls in [B,C,D]:
    try:
        raise cls()
    
    except B:
        print('B')
    except D:
        print('D')
    except C:
        print('C')

'''
THis is the real way of doing exception handling
if name of the error is not given then it works as
wildcard(means it handles all the exception.).
'''

import sys
try:
    with open('D:\Visual Studio 2017\Repos\PythonApplication3\PythonApplication3\exception_test.txt') as f:
        s= f.readline()
        i= int(s.strip()) # strip() returns the copy of string in which the defined characters are stripped from beginning and end.
except OSError as err:
    print('OS Error: {0}'. format(err))
except ValueError:
    print('Could not convert data to integer.')
except:
    print('Unexcepted Error: ', sys.exc_info()[0])
    raise
'''
 sys.exc_info gives information about the exception that is 
 currently being handled in the format (type, value, traceback)
'raise' displays the class object of error along with value 
'''
#Check
import sys
try: 
    a= 1/0
    c= '!!!cat!!!'
    b= int(c.strip('!'))
except: 
    print('Unexceptied Error ', sys.exc_info()[0])
    # raise

try:
    raise Exception('spam','eggs') # associated value or exception's argument
except Exception as inst: # inst is variable that represents exception instance
    print(type(inst))  # and the exception instance is bound to instance.args , type() returns the type of variable
    print(inst.args) #__str__ allows args to be printed as we know that print executes __str__()
    print(inst)      # but may be overwrritten

    x, y = inst.args #unpack args
    print('x =', x)
    print('y =', y)

# even functions can be called indirectly

def this_fails():
    x =1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error: ', err)
