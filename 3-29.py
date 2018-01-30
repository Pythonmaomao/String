# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:46:03 2018

@author: kanjingli
"""

gougou = ['gou','male',27,'wan']
maomao = ['maomao','female',25,'xuexi']
list_1 = [gougou,maomao]
print("用户可以进行增删改查操作")
#增加操作
list_1.append(['manong','male',2,'kanshu'])
list_1.insert(1,['mahua','female',1,'shuijiao'])
#修改
list_1[0][3] = 'wanyouxi'
#复制
list_2 = list_1.copy()
#删除
list_1.pop(0)
list_1.clear()
#查找

list_2 = [['gou', 'male', 27, 'wanyouxi'],
 ['mahua', 'female', 1, 'shuijiao'],
 ['maomao', 'female', 25, 'xuexi'],
 ['manong', 'male', 2, 'kanshu']]
for i in range(4):
    if int(list_2[i][2]) < 18:
        print(list_2[i])
for j in range(4):
    if list_2[j][0] == 'maomao':
        print(list_2[j])
        