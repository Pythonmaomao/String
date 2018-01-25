# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 11:24:38 2017

@author: kanjingli
"""
import sys
def test():
    args=sys.argv
    if len(args)==1:
        print('Hello,world!')
    elif len(args)==2:
        print('Hello,%s!'%args[1])
    else:
        print('Too many arguments!')
if __name__=='__main__':
    test()
def _private_1(name):
    return 'Hello,%s'%name
def _private_2(name):
    return 'Hi,%s'%name
def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)