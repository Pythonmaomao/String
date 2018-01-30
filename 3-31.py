# -*- coding: utf-8 -*-
"""
heroes beta-0.2
Created on Tue Jan 30 10:02:57 2018
milo str map if while 
格式化输出，利用列表打印地图，实现人物移动效果
@author: kanjingli
"""
welcome = 'welcome heroes world!'

mapmsg = '#######'
mapins = "\n-*-the world is like this-*-\n %s \n the '*' is you" %(mapmsg,)#元组只有一个元素用，
map = ['#','#','#','#','#','#','#']
instruction = '''
control your hero:
|'a'for left,'d'for right|'''
print(welcome)

name = input('input your name:')
hp = 100

if not name:
    name = 'player01'
usermsg={"name":name,'hp':hp}

print("your hero's name is:",usermsg['name'],'hp is',usermsg['hp'])
print(mapins,instruction)
point = 0
while 1:
    map[point] = "*"
    print("you are here","".join(map))
    userinput = input('go or quit:')
    if userinput == 'd'and point < 6:
        map[point] = '#'
        point += 1
    elif userinput == 'a'and point > 0:
        map[point] = '#'
        point -=1
    elif userinput == 'quit':
        print("goodbye!")
        break
    else:
        print(instruction)
#元组的方式设计地图
map = ((0,0),(1,0),(2,0)
,(0,1),(1,1),(2,1),
(0,2),(1,2),(2,2))

