# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 11:39:41 2018

@author: kanjingli
"""
# -*- coding: utf-8 -*-
"""
heroes beta-0.2
Created on Tue Jan 30 10:02:57 2018
milo str map if while 
格式化输出，利用列表打印地图，实现人物移动效果
@author: kanjingli
"""
import os
welcome = 'welcome heroes world!'
i = 0
while True:
    if os.path.isfile('lock.log'):
        print('locked')
        break
    username = input('login:')
    password = input('password:')
    i += 1
    if username == 'milo' and password == '123':
        pass
    else:
        if i == 3:
            open('lock.log','w').write(username)
            print('locked by %s'%username)
            break#结束
        continue#掉过后边的程序
    print(welcome)
    break
