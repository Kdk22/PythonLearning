for i in range(2, 20):
    for j in range(2, i):
           if i%j ==0:
               print(i, 'is not prime.')
               break
    else:
        print(i,'is prime number')

for i in range(0,20):
    if i %2 ==0:
        print(i,'is even')
        continue
print(i,'is odd')

a, b =0,1
while a<10:
    print(a)
    a,b= b, a+b