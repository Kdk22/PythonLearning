list(range(3,6)) #in python interactive
# what if you want to send list as an argument
args= [3,6]
list(range(*args)) # when arguments are in list or tuple then use '*' with arguments to unpack the arguments for function call

def Parrot(voltage, state='cuttent', action='Jhatkaa'):
    print('You got electric shock', voltage)
    print('Solar power ', state)
    print('He n\'s got powerful engine that gives' , action)

dic= {'voltage':1000, 'state':'current', 'action':'ghinieee'}
Parrot(**dic) #similarly we use ** for dictionaries
