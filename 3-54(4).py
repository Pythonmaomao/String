#抛出异常
'''try:
    f = open('hannuo.py','r')
    fr = f.read()
    print(fr)
finally:#无论什么情况都会执行关闭程序
    f.close()
    '''

with open('hannuo.py','r') as f:
    f.read()#with....as....自动close语句
if 0:#抛出异常
    raise NameError('your name error!!!')
l = [1]
assert len(l),'changdu'#0=false,根据表达式来给出异常，如果是true则没有异常，false则显示异常

