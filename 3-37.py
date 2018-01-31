def machine(x, y='naiyou', *arg):
    print('制作一个%d元的%s味道的冰激凌' % (x, y))
    print('arg:', arg)
#如何处理序列*d
l = [5, '巧克力']
machine(*l)
#制作一个5元的巧克力味道的冰激凌
#如何处理字典**d
d = {'x': 5, 'y': '薄荷'}
machine(**d)
#制作一个5元的薄荷味道的冰激凌
#d = {'x': 5, 'z': '薄荷'}z变量不一致无法执行
#machine(**d)
machine(3, 5)
#制作一个3元的5味道的冰激凌
#冗余变量如何处理
def machine(x, y='naiyou', *arg):
    print('制作一个%d元的%s味道的冰激凌' % (x, y))
    print('arg:', arg)


machine(3, 5)
#制作一个3元的5味道的冰激凌
#arg: ()
machine(3, 5, 7)
#制作一个3元的5味道的冰激凌
#arg: (7,)
machine(y=5, x=3)
#制作一个3元的5味道的冰激凌
#arg: ()

#冗余变量字典处理
def machine(x, y='naiyou', *arg, **kv):
    print('制作一个%d元的%s味道的冰激凌' % (x, y))
    print('arg:', arg)
    print('kv:', kv)
machine(y=5, x=3, z=7)
#制作一个3元的5味道的冰激凌
#arg: ()
#kv: {'z': 7}
