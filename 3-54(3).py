#异常处理
try:
    s = 'hello'
    print(s[0])
except IndexError:
    print('error')
else:#没有异常执行
    print('no error')
