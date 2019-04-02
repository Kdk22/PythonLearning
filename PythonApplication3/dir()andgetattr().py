class Person:
    name= 'Peter'
    age= 30

print(getattr(Person, 'name')) # worked
print(Person.name) #worked

person = Person()

print(getattr(person, 'name')) # worked
print(getattr(person, 'age', 0)) #worked
print(getattr(person, 'sex', 'Male')) # default value is male
# print(getattr(person, 'Maritial Status')) #No default value 'AttributeError
# print(getattr(person, 'name')('Hello'))

setattr(person, 'name','Allen') # allows to set attribute of an object

print(getattr(person, 'name')) # only instance attribute is changed. Output is 'Allen'
print(getattr(Person, 'name')) # class attribute remains as it is. Output is 'Peter'


'''
 # when class attribute is changed
setattr(Person, 'name','Alex') # Person is class attribute
print(getattr(Person, 'name')) # Output is alex

print(getattr(person, 'name')) # Output is alex

'''
obj =1000
for attr_name in dir(obj):
    attr_value= getattr(obj, attr_name)
    print('Attribute name is ', attr_name)

    print(' and its value is ',attr_value)

    print(' Is it callable? ', callable(attr_value))

    # print(attr_name, attr_value, callable(attr_value))


print(getattr(obj, 'bit_length')()) # bit_length is in dir(obj) and it's a built- in method of int type and it is callable you can find it in output



'''
ref: 
https://stackoverflow.com/questions/4075190/what-is-getattr-exactly-and-how-do-i-use-it
https://www.programiz.com/python-programming/methods/built-in/getattr
'''
