# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:25:51 2017

@author: kanjingli
"""
from collections import Iterator
isinstance((x for x in range(10)),Iterator)
isinstance([],Iterator)
isinstance({},Iterator)
isinstance('abc',Iterator)
isinstance(iter([]),Iterator)
for x in[1,2,3,4,5]:
    pass
it=iter([1,2,3,4,5])
while True:
    try:
        x=next(it)
    except StopIteration:
        break
def product(start,end,handle):
    total=1
    for x in range(start,end+1):
        total*=handle(x)
    return total
def identity(n):
    return n
def factroial(n):
    return product(1,n,identity)
f=abs
f(-10)
def add(x,y,f):
    return f(x)+f(y)
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
list(map(str,[1,2,3,4,5,6,7,8,9]))
from functools import reduce
def add(x,y):
    return x+y