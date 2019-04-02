import json
''' Here this 'Json Object'(inside Serialization.txt) looks like a dictionary of python but it's not
because bollean value true and false are in small letters ( True and False
is written in Python) and null is written,However in python it is written as 'None'.
It is json object therfore it is not written here in .py file.
'''

# The Json Object 'movie info' is inside Serialization.txt
'''Here 'person_info' is a python dictionary
as you can see True , False and None in it.So,
it can be complied by python interpreter
'''
person_info= {
   'name': 'Jhon',
    'age': 30,
    'married': True,
    'divorced': False,
    'children': ('Ann', 'Billy'),
    'pets': None,
     'cats': [
         {'model': 'BMW 230', 'mpg': 27.5},
         {'model': 'Ford Edge','mpg': 24.1}
         ]
    }


with open('D:\Visual Studio 2017\Repos\PythonApplication3\PythonApplication3\Deserialization.txt','r+',encoding='utf-8') as f:
    movie_data = json.load(f) #converts json object into python dict and displays output
   # person_data= json.dump(person_info,f,indent=4, sort_keys= True) #converts Python dict into Json object and stores in file
    

print(movie_data["title"]) #you can even access the data by key

with open('D:\Visual Studio 2017\Repos\PythonApplication3\PythonApplication3\Serialization.txt','r+') as f:
    person_data= json.dump(person_info,f, indent=4,sort_keys=True) #dumped into Serialization.txt file
    pointer_position=f.tell()
    #sot_keys specifies if the result should be sorted or not
    
    

    #if you want dump in ceratain position you run the program then use seek() and tell()

print(pointer_position)
print('Here is the output of load() ,\n which is Python dicionary.Initially it was Json Object')
print(movie_data)
print(type(movie_data))

print('here is the output of dump(),\n here Python Dict is taken to file \n stored as Json object')
print(person_data)
print('It\'s type when it was written in Python', type(person_info), 'and now it is converted to JSON Object.')
print(type(person_data))


