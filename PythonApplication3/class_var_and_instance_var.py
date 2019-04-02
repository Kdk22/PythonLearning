
class foo:
    x='orginal class'

c1,c2 = foo(), foo()
''' THis is creating the multiple objects of
    same as 
    c1 = foo()
    c2 = foo()
    and these objects can access class variable (or name)
'''

print('Output of c1.x: ', c1.x)
print('Output of c2.x: ', c2.x)
'''
    Here if you change the c1 instance, and it will 
    not affect the c2 instance
'''
c1.x = 'changed instance'

print('Output of c1.x: ',c1.x)
print('Output of c2.x: ',c2.x)

'''
    But if I change the foo class, all instances of that
    class will be changed 
'''

foo.x = 'Changed class'

print('Output of c1.x: ',c1.x)
print('Output of c2.x: ', c2.x)
'''
    Now using 'self'
    Here Changing the class does not affect the instances
'''
class foo:
    def __init__(self):
        self.x = 'Orginal self'

c1 = foo
foo.x ='changed class'
print('Output of instance attributes: ', foo.x)
print('Output of self: ',c1.x)

# ref: https://stackoverflow.com/questions/1537202/variables-inside-and-outside-of-a-class-init-function