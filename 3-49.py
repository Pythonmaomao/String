#重载父类方法
class Father:
    money = 1000000
    __money = 100000000#私有属性无法继承调用
    def drive(self):
        print('I can drive a car!')
class Mother:
    money = 10000

class Son(Father,Mother):
    pass
    def drive(self):#重载父类方法
        print('I can drive tank!')
        Father.drive(self)#直接调用父类的方法
    def pay(self):
        print(self.money)#两个相同的只继承第一个
        print(self.money)
tom = Father()
print(tom.money)
tom.drive()
print('#'*50)
jerry = Son()
print(Son.money)
jerry.drive()
jerry.pay()