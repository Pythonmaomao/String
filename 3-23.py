for i in range(10):
    if i == 5:
        print(i*10)
        continue#满足后边的程序不执行
    if i == 7:
        break#满足跳出当前循环
    if i == 2:
        pass#占位符，不做任何操作
    print(i)