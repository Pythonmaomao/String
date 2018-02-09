class Human:
    '''
       this is the Human class!!!
    '''
    name = 'ren'
    __money = 100
    def __init__(self,name,age):#对象实例化后init函数自动执行
        print('#'*50)
        self.name = name#只是赋值，没有输出打印;传入实例的属性
        self.age = age
        print('#'*50)
    #@classmethod#类方法
    @property
    def say(self):#公有方法，有self参数
        print("my name is %s i have %s"%(self.name,self.__money))
        return self.name
    @staticmethod#静态类方法，装饰器
    def bye():#公有方法，不用self参数
        print("GAME OVER")

#Human.bye()#通过类直接访问,不用加装饰器也能调用
#tom = Human('name',20)
#tom.bye()#有了装饰器通过对象访问
#Human.say()#通过类直接访问
#tom = Human('name',20)
#tom.say()#有了装饰器通过对象访问
#x = Human.say()
#print(x)
tom = Human('tom',20)
print(tom.say)#property方法变属性
#print(Human.say)#property方法变属性