# String
String manipulation
#让用户输入字符，寻找‘f’、‘r’、‘i、‘e’、‘n’、‘d’字符个数，如果所有字符都有，打印字符‘friend’。并输出可以组合多少个friend。
# -*- coding: utf-8 -*-
a=input("plz input a string :")
a1 = a.count('f')
a2 = a.count('r')
a3 = a.count('i')
a4 = a.count('e')
a5 = a.count('n')
a6 = a.count('d')
if a1 and a2 and a3 and a4 and a5 and a6 :
    print("friend")
    print("there are %d 'friend'"%(min(a1,a2,a3,a4,a5,a6)) )
