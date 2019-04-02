def func(a,b,c,d):
    print(a,b,c,d)

def func2(*arg):
    #this is what i want to do
    args=list(arg)
    args[0]='We'
    args[2]='Are you gar?'
    print('-'*20,' output of list', '-'*20)
    func(*args) #unpacking
    # But I used loop
    for a in arg:
        print('-'*20, 'Output of Loop','-'*20)
        print(a)
#        arg[0]='We' # since tuples are immutable
#         arg[2]='are you gay?' # Item assignment is not supported in tuple
        
        print(a[0])
        #  print(a[2])
        print(arg[3])
    l=list(arg)

    func(*l)

func2('Do','I think you had fun','Are you girl?','No! I am not')

# THis is for Command Line Mode (Interactive)
charles={'name': Charles, 'Born': 1832}
lewis = charles
lewis= charles
lewis is charles
id(lewis), id(charles)
Lewis['balance'] =950
charles

alex={'name': Charles,'Born': 1832}
alex== charles
alex is not charles
