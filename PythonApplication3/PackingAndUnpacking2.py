def function1(a,b,c,d):    
    print(a, b, c, d)

def function2(*args):
    arg= list(args)
    arg[0]= 'I want to '
    arg[1]= 'know '
    arg[2]= 'you'
    print(arg[0])
    function1(*arg)

function2('I ','am', 'stucked', 'becz ', 'you are beautiful')
