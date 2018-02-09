class Person:
    '''
       this is the Human class!!!
    '''

    def __init__(self,first_name,last_name):#对象实例化后init函数自动执行

        self.first_name = first_name#只是赋值，没有输出打印;传入实例的属性
        self.last_name = last_name
        print('#'*50)
    #@classmethod#类方法
    @property
    def full_name(self):#公有方法，有self参数

        return "%s %s" %(self.first_name,self.last_name)
#fl = Person('milo','zou')#不加装饰器时
#flname = fl.full_name()
#print(flname)
fl = Person('milo','zou')#加装饰器时
fl.first_name = 'qixian'#改名字
print(fl.full_name)