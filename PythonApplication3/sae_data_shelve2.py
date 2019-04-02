import shelve

with shelve.open('D:\Visual Studio 2017\Repos\PythonApplication3\PythonApplication3\save3.db',flag='c') as f:
    f['names']=['Mohit','Ravi','Bhaskar']
    f['skills']=['Python','Java','R#']
    f['age']=[27,25,26]

    print(f['names'])
    print(f['skills'])
    print(f['age']) 
  
print('-'*40, 'FOR LOOP AND KEY', '-'*40)    
with shelve.open('D:\Visual Studio 2017\Repos\PythonApplication3\PythonApplication3\save3.db',flag='r') as f:
    for key in f:
        print(f[key])

with shelve.open('D:\Visual Studio 2017\Repos\PythonApplication3\PythonApplication3\save3.db', flag='w',writeback=True) as f:
    key1 = input('Enter the key\n')
    val1 = int(input('Define the number of values to be passed in key1: '))
    list=[]
    for x in range(val1):        
        val = input('\nEnter value for each position :')
        list.append(val)
        #val_list.append(val)
    f['key1']= list
    print(f['key1'])

    with shelve.open('D:\Visual Studio 2017\Repos\PythonApplication3\PythonApplication3\save3.db', flag='r') as f:
        key1 = input('Enter the key\n')    
        print(f[key1]) 

# ref: http://l4wisdom.com/python/python_shelve.php