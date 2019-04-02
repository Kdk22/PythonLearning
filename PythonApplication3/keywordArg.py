def Parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print('__ This parrot would n\' t', action, end=' ')
    print('If you put ', voltage , ' vots through it.')
    print('__ lovely plumage, the', type)
    print('--It n\' s', state)
    print('Itn\'s', voltage, 'wonderful', state , 'for bikern\'s to ', action, ' in ' , type)

Parrot(1000)
Parrot(voltage= 2000)
Parrot(voltage= 5000, action= 'Broom Broom')
Parrot('a millioon','thouseads','Dollars')
# Parrot('Dead', voltage='6000') #it gives type error