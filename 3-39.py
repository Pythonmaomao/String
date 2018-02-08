#匿名表达式lambda
from functools import reduce
def f(x,y):
    return x+y
c = reduce(f,[1,2,3,4,5])
print(c)
ff = lambda x,y:x+y
d = ff(2,3)
print(d)
g = reduce(lambda x,y:x-y,[1,2,3,4,5])
print(g)
