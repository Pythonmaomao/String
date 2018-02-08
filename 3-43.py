#一个函数装饰另一个函数
import time
def deco(func):
    def wrapper():
        startT = time.time()
        func()
        endT = time.time()
        msecs = (endT - startT) * 1000
        print("it's %f ms" % msecs)
    return wrapper
@deco#装饰器
def myfunc():

    print('myfunc start.....')
    time.sleep(1.7)#停顿1.7秒钟
    print('myfunc end....')

print("myfunc is ",myfunc.__name__ )
#myfunc = deco(myfunc)
print('#'*50)
print("myfunc is ",myfunc.__name__ )
myfunc()