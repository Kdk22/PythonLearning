# ref: https://www.programiz.com/python-programming/methods/string/format
# ref: https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
#number formatting
print('The number is :{:d}'.format(123))
print('THe float is :{:10.3f}'.format(12.2346))
print('bin: {0:b}, oct:{0:o}, hex:{0:x}'.format(12))
# with padding
print('{:5d} is a number'.format(12))
print('{:10} is a string'.format('Pyception'))
'''
By default strings are left-aligned,
whereas numbers are right-aligned with in the field
'''
print('{:8.3f}'.format(12.2346))
print('{:08.3f}'.format(12.2346))

#number formatting for signed numbers
#show - sign only.
print('{:-f}{:-f}'.format(12.23,-12.23))

#integers left aligned filled with 0
print('{:<05d}'.format(12))

#str.zfill() does the same
'12'.zfill(5)

#forces -sign to left most
print('{:=8.3f}'.format(-12.2346))

#string padding with center alignment
# and '*' padding character
print('{:*^5}'.format('cat'))

# formating class
class Person:
    name= 'Adam'
    age = 23

print('{p.name} is of age: {p.age}'.format(p=Person()))

#formating dic
person={ 'name':'Adam', 'age':23 }
print('{p.name} is of age: {p.age}'.format(p=Person()))
print('{name} is of age {age}'.format(**person))
#** is keyword arguments

table ={'Sjoerd': 4127, 'Jack': 4098,'Dcab':8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab:{0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab:{Dcab:d}'.format(**table))

#Dynamic formatting
#'dynimic string format template' must be defined
string='{:{fill}{align}{width}}' #format
print(string.format('cat',fill='*', align='^', width=5))

num='{:{align}{width}.{precision}f}' #format
print(num.format(123.236, align='<', width=8, precision=2))

for i in range(1,11):
    print('{0:1d},{0:3d},{0:4d}'.format(i,i*i,i*i*i)) #there would no space at begining
    # analyze the difference
for i in range(1,11):
    print('{0:2d},{0:3d},{0:4d}'.format(i,i*i,i*i*i)) # there would be sapce at beginning

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4)
    # str.rjust() str.ljust() and str.center() are for right-adjust, leftadjust and center 
