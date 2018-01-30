# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 11:02:00 2018

@author: kanjingli
"""
'''
x = int(input("first:"))
o = input('operator:')
y = int(input("second:"))
if o == "+":
    print(x + y)
elif o == '-':
    print(x - y)
elif o == '*':
    print(x * y)
elif o == '/':
    print(x/y)
else:
    pass
'''
x = int(input("first:"))
o = input('operator:')
y = int(input("second:"))
operator = {
            '+':x+y,
            '-':x-y,
            '*':x*y,
            '/':x/y}
result = operator.get(o,'please input +|-|*|/')#取%不报错
print(result)
