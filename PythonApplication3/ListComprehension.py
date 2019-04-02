
'''
List comprehensions provide a concise way to create lists. 
Common applications are to make new lists where each element 
is the result of some operations applied to each member of 
another sequence or iterable, or to create a subsequence of
those elements that satisfy a certain condition.

'''

square=[]
for i in range(0,10):
    square.append(i**2)

''' This is to implemented in python interactive.
Here this piece of code still store the value of i (i=9)
even after the loop is fully executed and all the works are completed
'''


'''These are the best way of list comprehension'''
square = list(map(lambda x: x**2, range(10)))

square = [x**2 for x in range(10)]

'''
These codes doesnot stores the value of x after
the execution is complete. The reduces the memory
'''

matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    ]
[[row[i] for row in matrix] for i in range(4)]

'''THis one below is the simplified form '''

k=[]
for i in range(4):
    l=[]
    print('i: ',i)
    for row in matrix:
        print('row is: ',row)
        print('row[i] is' ,row[i])

        l.append(row[i])
        print('l: ' ,l)

    k.append(l)
    print('k: ',k)
print(k)


'''The simplest form above all these codes. There is function called 'zip(*iterables)'  '''

print(list(zip(*matrix))) # here elements of list matrix is unpacked to zip function