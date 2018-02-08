def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
'''def f():
    print('one')
    yield 1
    print('two')
    yield 2
    print('three')
    yield 3
    '''
g = fib(8)#g[1,2,3]生成器最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
k = g.__next__()
l = g.__next__()
v = g.__next__()
print(k)
print(l)
print(v)
