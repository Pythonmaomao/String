#方法重载。自定义类，对象为列表，可以做加减乘除运算，本身列表不能做运算
class MyList:
    __mylist = []
    def __init__(self,*args):
        self.__mylist = []#返回私有属性值的方法
        for arg in args:
            self.__mylist.append(arg)
    def __add__(self,x):
        for i in range(0,len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] + x
        #print(self.__mylist)
        return self.__mylist


    def __sub__(self,x):
        for i in range(0,len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] - x
        #print(self.__mylist)
        return self.__mylist
    def __mul__(self,x):
        for i in range(0,len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] * x
        #print(self.__mylist)
        return self.__mylist

    def __truediv__(self,x):
        for i in range(0,len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] / x
        #print(self.__mylist)
        return self.__mylist

    def __mod__(self,x):
        for i in range(0,len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] % x
        #print(self.__mylist)
        return self.__mylist
    def __pow__(self,x):
        for i in range(0,len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] ** x
        #print(self.__mylist)
        return self.__mylist
        pass
    def __len__(self):
        pass

    def show(self):
        print(self.__mylist)


if __name__ == '__main__':#而在执行之前会根据当前运行的模块是否为主程序
    # 而定义变量__name__的值为__main__还是模块名。因此，该判断语句为真的时候，说明当前运行的脚本为主程序，而非主程序所引用的一个模块。这在当你想要运行一些只有在将模块当做程序运行时而非当做模块引用时才执行的命令，
    # 只要将它们放到if __name__ == "__main__:"判断语句之后就可以了。

    l = MyList(1,2,3,4,5)
    l + 10
    l.show()
    l ** 10
    l.show()