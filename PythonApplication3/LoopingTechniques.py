knights={'galland':'the pure','robin': 'the brotherhood'}
for k, v in knights.items():
    print(k,v)
    '''the position index and corresponding
   value can be retrived usnig enumerate()
   function'''

t=['THis','world','is','not','real']
for k, v in enumerate(t):
    print(k,v)

questions=['name','address','phone','sex','Work']
answers=['Latina','Las Vegas','+91-983859483','Female','Escort']
for q, a in zip(questions,answers):
    print('What is your {0} ? Itn\'s {1} . '.format(q,a) )

for i in reversed(range(1,10,2)):
    print(i)

import math
straight=[2.40,3.40,4.60,6.90,float('NaN'),2.10, float('NaN')]
filtered=[]
for i in straight:
    if  not math.isnan(i): # checks either it is number or not( is Not a Number)
        filtered.append(i)
print(filtered)