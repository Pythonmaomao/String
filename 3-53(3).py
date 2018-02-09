#通过装饰器，使用类中的内置属性取值，赋值
from decimal import Decimal
class Fees(object):
    def __init__(self):
        self.__fee = None
#----------------------------------------------------
    @property#取值的装饰器，property本身是只读的，通过函数实现取值、赋值
    def fee(self):
        return self.__fee
    @fee.setter#赋值的装饰器
    def fee(self,value):
        if isinstance(value,str):
            self.__fee = Decimal(value)
        elif isinstance(value,Decimal):
            self.__fee = value
if __name__ == '__main__':
    f = Fees()
    f.fee = '10'#赋值
    print(f.fee)#直接用内置属性解决，不用调用函数