def f(a,L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def g(a, L=None):
    if L== None:
        L=[]
        L.append(a)
    return L
print(g(4))
print(g(5))

