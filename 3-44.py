#闭包,（函数中定义一个函数），传递变量使得：值和函数捆绑在一起,新函数调用上层函数的参数
def hello_conf(prefix):
    def hello(name):
        print(prefix,name)
    return hello
a = hello_conf('Good morning!')
print(a.__name__)
print(id(a))
a('milo')
a('maomao')
b = hello_conf('Good afternoon!')
print(b.__name__)
print(id(b))
b('maomao')