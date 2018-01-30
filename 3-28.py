# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:17:40 2018

@author: kanjingli
"""

nums = []
for i in range(1,10):
    if i%3 ==0 or i%5 == 0:
        nums.append(i)
print(nums)
print(sum(nums))
#简化后#列表表达式，列表解析，对序列操作生成新的列表
k = [i for i in range(1,10) if i%3 == 0 or i%5 == 0]
print(sum([i for i in range(1,10) if i%3 == 0 or i%5 == 0]))
#生成表达式，[]-()延迟求值，惰性运算，不生成列表，生成generator object,调用时才会生成值，加快计算速度
print(sum((i for i in range(1,10) if i%3 == 0 or i%5 == 0)))

l = (i for i in range(1,10) if i%3 == 0 or i%5 == 0)
for i in l:
    print(i)