class Car():
    '''汽车类'''
    color = 'black'#属性
    def run(self):#self代表对象本身，不需要传递参数
        '''方法'''
        print('go go go!')
    def stop(self):
        print('stoooooop!')
bmw = Car()
bmw.color = 'red'
print(bmw.color)
bmw.run()