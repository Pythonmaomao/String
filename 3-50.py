#私有属性赋值
class C1():
    __x = 0
    def meth1(self):
        self.__x = 10
        return self.__x#不加无法返回

C = C1()
print(C.meth1())
