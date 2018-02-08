'''类中的属性和方法；对应的变量和函数'''
class Human:
    '''
       this is the Human class!!!
    '''
    name = 'ren'
    gender = 'male'
    age = '25'
    __money = 8000#__表示私有属性，内部属性,私有属性外部无法调用
    def __init__(self,name,age):#对象实例化后init函数自动执行
        print('#'*50)
        self.name = name#只是赋值，没有输出打印;传入实例的属性
        self.age = age
        print('#'*50)
    def __str__(self):#魔法方法，可以执行对象的属性
        msg = 'hi! I am the object of Human'
        return msg
    def say(self):#公有方法
        print("my name is %s i have %s"%(self.name,self.__money))
        self.__lie()
    def __lie(self):
        print('i have 5000')

#zhangsan = Human()
#zhangsan.name = 'zhangsan'
#print(zhangsan.name)
#print(zhangsan.__money)#私有属性外部无法调用
#zhangsan.say()#只能通过公有函数来调用
#zhangsan.__lie()#私有方法外部无法调用

zhangsan = Human('zhangsan',30)#对象实例化后init函数自动执行有了init函数后，可以直接执行
print(zhangsan.name,zhangsan.age)
print(zhangsan)#有了魔法方法，可以打印对象
print(Human.name)#有了魔法方法，可以打印类的属性
#print(Human.__money)#有了魔法方法，不可以内部属性
print(Human.__doc__)#doc内置属性，不用定义，打印类中字符串docstring

