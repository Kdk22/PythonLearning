import shelve
import pickle
from Player import Player

items =['Khuda','Khukuri','Crowbar']

my_obj = Player(1,'Kylian Mbappe',100.0,items)
print(my_obj)

with shelve.open('D:\Visual Studio 2017\Repos\PythonApplication3\PythonApplication3\save2.db','c') as out_file:
    out_file['Data']= my_obj
    #out_file[Player.name]= 'Kylian Mbappe',
    #out_file[Player.health]= 100,
    #out_file[Player.items]= items

print('________________________________OUTPUT VIA SHELVE________________________________')

with shelve.open('D:\Visual Studio 2017\Repos\PythonApplication3\PythonApplication3\save2.db','r') as out_file:
    player_data= out_file['Data']
   # player_name= out_file[Player.name]
    #new_obj = shelve.load(out_fil)

print(player_data)
#print(player_name)
