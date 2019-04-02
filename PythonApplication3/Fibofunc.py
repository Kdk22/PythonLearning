def fib(n):
    a,b= 0,1
    while a<n:
        print(a)
        a,b= b, a+b
        print()

fib(100) 

def fib2(n):
   result = []
   a, b = 0, 1
   while a < n:
       result.append(a)
       a, b = b, a+b
   return result

fib2(100)

def ask(prompt, retries=4, reminder='Please try again !'):
    while True:
        ok= input(prompt)
        print(ok,'is here')
        if ok in ('y','ye','yes'):
            return true
        if ok in ('N','No','Na','Nope'):
            return false
        retries= retries-1
        if retries<0:
            raise ValueError('invalid user response')
        print(reminder)
ask('yes')






   