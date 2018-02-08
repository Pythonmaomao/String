#自定义类，对象为列表，可以做加减乘除运算，本身列表不能做运算
class MyList:
    __mylist = []
    def __init__(self,*args):
        self.__mylist = []
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
        pass
    def __div__(self,x):
        pass

    def __mod__(self):
        pass
    def __pow__(self):
        pass
    def __len__(self):
        pass

    def show(self):
        print(self.__mylist)


if __name__ == '__main__':

    l = MyList(1,2,3,4,5)
    l + 10
    l.show()
    #l - 10
    #l.show()