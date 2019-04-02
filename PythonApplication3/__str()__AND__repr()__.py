# shorthand of __str__() and __repr__() are !s and !r
print('Quotes: {0!r}, Without Quotes: {0!s}'.format('Cat'))

# 0 indicates Cat
# __str()__ and __repr__() implementation for class

class Person:
    def __str__(self):
        return "STR"
    def __repr__(self):
        return "REPAR"

print('repr: {p!r}, str: {p!s}'.format(p=Person()))

#datetime formatting
import datetime
date= datetime.datetime.now()
print('Time is: {:%Y/%m/%d %H:%M:%S}'.format(date))

#overriding __format__() .It's a custom __format__() method
class Person:
    def __format__(self, format):
        if(format=='age'):
            return '23'
        return 'None'
print('Adam\'s age is :{:age}'.format(Person()) )