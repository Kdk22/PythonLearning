class Employee:
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):

   raise_amt = 1.10
   
   def __init__(self, first, last, pay, prog_lang):
       super().__init__(first, last, pay) 
       #Employee.__init__(self, first, last, pay) #Or if super is not used
       self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        print('Insiede self.employees: ' ,employees)
        super().__init__(first,last, pay)
        if employees == None:
            self.employees = []
            print('Inside self.employee: ', self.employees)
        else:
            self.employees = employees
        print('Employee object: ',employees)
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
           # print(self.employee[emp])
            #print(sef.employee(emp))
            print('Emp object: ', emp)
            print('Emp Name: ', emp.fullname())
           # print('In print_emp Self.employees: ', self.empoyees)
dev_1 = Employee('Corey','Schafer', 5000)
dev_2 = Employee('Testee', 'Employaa', 6000)

dev_1.apply_raise()
print(dev_1.pay)


'''
    if you put pass inside Developer class and do not define 
    __init__ function then it will directly run the Employee 
    class but if you define __init__ function then Developer object
    runs __init__ function first and then Employee second. Arguments
    passed inside the developer object would be passed into __init__ 
    method of Developer class not inside the __init__ method of Employee 
    class but if there is only pass statement inside Developer class 
    then arguments passed inside developer object would be passed
    directly inside Employee class

'''
dev3 = Developer('Corey','Schafer',5000, 'python')
dev4 = Developer('Teseer', 'Sake',6000 , 'Tensorflow')
print('Dev3 Object: ', dev3)
print('Dev4 Object: ', dev4)
dev3.apply_raise()
print(dev3.pay)

print(dev3.fullname())
print(dev_1.email)
print(dev_2.email)

print(dev3.email)
print(dev4.email)

print(dev3.prog_lang)
print(dev4.prog_lang)

#print(help(Developer))

mgr_1 = Manager('Sue', 'Smith', 90000, [dev4])
mgr_1.add_emp(dev4)
print(mgr_1.email)
mgr_1.print_emp()

#ref: https://www.youtube.com/watch?v=RSl87lqOXDE