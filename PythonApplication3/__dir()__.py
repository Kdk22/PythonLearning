
import sys
print('Here are the all the attributes')
print(dir(sys))
function = input('Enter the name of function: ')

if function in dir(sys):
    print(function ,'lies in sys')
else: 
    print('Please enter valid attribute name')


   
print(dir(getattr(sys, function)))


# another way done in stackoverflow
'''
import sys
print('Here are the attributes of sys')
print(dir(sys))
attr= input('Enter the name of attribute:')

ctc= True
while ctc:
    if attr in dir(sys):
        print(attr, 'lies inside sys.')
        ctc= False
    else:
        print('Invalid attribute')
        ctc= True

print(dir(getattr(sys,attr)))
'''