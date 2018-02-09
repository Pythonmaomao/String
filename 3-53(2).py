#类中的内置属性取值，赋值
from decimal import Decimal
class Fees(object):
    def __init__(self):
        self.__fee = None
#----------------------------------------------------
    def get_fee(self):
        return self.__fee
    def set_fee(self,value):
        if isinstance(value,str):
            self.__fee = Decimal(value)
        elif isinstance(value,Decimal):
            self.__fee = value
    fee = property(get_fee,set_fee)#装饰器的方法
#fee = Fees()
#print(fee.get_fee())#取值
#fee.set_fee('10')#改值
#print(fee.get_fee())
f = Fees()
f.set_fee('10')#装饰器不用get_name()就可以赋值
print(f.fee)#多了fee的属性