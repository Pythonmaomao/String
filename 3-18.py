# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:58:29 2018

@author: kanjingli
"""
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