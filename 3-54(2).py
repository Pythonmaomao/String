from heros import *#heros模块名字
msg = '欢迎来到 英雄无敌的世界。。。。！'
if __name__ == '__main__':
    print(msg)
    milo = Hero('milo')
    boss = Element('boss')
    print(boss.hp)
    milo.hit(boss)
    print(boss.hp)#怪物的hp-英雄的攻击力act'''
