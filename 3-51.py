#经典类 纵深访问
'''
class AA:
    def __init__(self):
        print("enter A")
        print("leave A")
class B(AA):
    def __init__(self):
        print("enter B")
        AA.__init__(self)
        print("leave B")
class C(AA):
    def __init__(self):
        print("enter C")
        AA.__init__(self)
        print("leave C")
class D(B,C):
    def __init__(self):
        print("enter D")
        B.__init__(self)
        C.__init__(self)
        print("leave D")
d = D()'''

#新式类,super(当前自己类的名字,self)先水平再向上
class AA:
    def __init__(self):
        print("enter A")
        print("leave A")
class B(AA):
    def __init__(self):
        print("enter B")
        super(B,self).__init__()
        print("leave B")
class C(AA):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")
class D(B,C):
    def __init__(self):
        print("enter D")
        super(D, self).__init__()
        print("leave D")
d = D()