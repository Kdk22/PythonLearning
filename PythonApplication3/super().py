# ref: https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance

class First:
    def __init__(self):
        super().__init__()
        print('First')

class Second:
    def __init__(self):
        #super().__init__()
        print('Second')

class Third(First, Second):
    def __init__(self):
        super().__init__()
        print('Third')

t = Third()

#ref: nbviewer.ipython.org/github/brentpayne/learning-python/blob/master/MixInMultipleInheritance/MixInMultipleInheritance.ipynb
class A:
    def __init__(self, s , *args, **kwargs):
        print('A: init:s[{0}]'.format(s))
        kwargs['s']= s
        
        self.s = s

class MixInF:
    def __init__(self,u, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        print('IObject: init')
        print('MixInF: init:u[{0}]'.format(u))
        for items in args:
            list = [items]
            print('Items in args: ', list)
        super().__init__(*args, **kwargs)      
    def f(self, y):
        print('IObject:y[{0}]'.format(y))

class B(MixInF):
    def __init__(self, v, *args, **kwargs):
        print ('B:init:v[{0}]'.format(v))
        kwargs['v']=v
        super().__init__(*args, **kwargs)
        self.v=v
    def f(self, y):
        print('B:f:v[{0}]:y[{1}]'.format(self.v,y))
        super().f(y)

class C(MixInF):
    def __init__(self, w, *args, **kwargs):
        print('C:init:w[{0}]'.format(w))
        kwargs['w']=w
        super().__init__(*args, **kwargs)
        self.w =w
    def f(self, y):
        print('C:f:w[{0}]:y[{1}]'.format(self.w, y))
        super().f(y)

class Q(C,B,A):
    def __init__(self, v,w, *args, **kwargs):
        super().__init__( *args, *kwargs)
        print('THis is me')
    def f(self, y):
        print('Q:f:y[{0}]'.format(y))
        super().f(y)

q= Q(5,6,7,8, 9,10,11)
q.f(15)
print(Q.mro())
print(C.mro())