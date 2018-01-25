# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:29:39 2018
heroes 0.1
@author: kanjingli
"""
hp = 100
print('welcome heroes world!')
print("|the world is like this ##### ,'a'for left,'d'for right|")
name = input('input your name:')
if not name:
    name = 'player01'
usermsg=[name,hp]

print("your hero's name is:",usermsg[0],'hp is',usermsg[1])
print("and now you are here:*####|'a'for left,'d'for right|")
userinput = input()
if userinput == 'd':
    print("you are here #*###")
if userinput == 'a':
    print("you are here *####")