employee = {'Alex':20000, 'Alen':300000,'Haven':300000,'Della':450000,}
print('Before calling function: ', employee)
def test(employee):
    new={'Dora':450000,'Dolex':34000,'Nolan':30000000}
    employee.update(new)
    print('Inside function test:', employee)
    return employee

el=test(employee)
print('THis is el:',el)
print('Outside function test:', employee)

