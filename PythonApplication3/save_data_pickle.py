import pickle
from Player import Player


items= ['axe','sword','gun']

my_obj = Player(1,'Luka Madrid',100.0, items)
print(my_obj)

with open('D:\Visual Studio 2017\Repos\PythonApplication3\PythonApplication3\save2.pkl','wb') as out_file:
    pickle.dump(my_obj, out_file, pickle.HIGHEST_PROTOCOL)

print('_____________________Output VIA PICKLE_____________________________')
with open('D:\Visual Studio 2017\Repos\PythonApplication3\PythonApplication3\save2.pkl','rb') as in_file:
    new_obj = pickle.load(in_file)

print(new_obj)

'''
 ref:https://www.youtube.com/watch?v=ifKintlPE_A
 '''