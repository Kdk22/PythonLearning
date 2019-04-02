import pickle
'''
When I named this file as 'pickle.py' then
it gave Attribute Error: module 'pickle' has no attribute 'dump'
then I changed name into pickle_copy.py. It worked afrer that.
THis is because 
import pickle
print(pickle.__file__)
C:\Program Files\Python36\lib\pickle.py
There is already a pickle module therefore it didn't worked.
'''
dict1={'a': 100,
       'b': 200,
       'c': 300
    }
list1=[400,500,600]

print(dict1)
print(list1)

#f= open("D:\save1.py",'wb')
with open("D:\Visual Studio 2017\Repos\PythonApplication3\PythonApplication3\save1.pkl",'wb') as f:
    pickle.dump(dict1, f)
    pickle.dump(list1, f)
#f.close()
print('_____________________________________')

with open("D:\Visual Studio 2017\Repos\PythonApplication3\PythonApplication3\save1.pkl",'rb') as f:
    dict_load= pickle.load(f)
    list_load = pickle.load(f)

print(dict_load)
print(list_load)