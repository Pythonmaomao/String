# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>0:
        return x
    else:
        return
import math
def mov(x,y,step,angle=0):
    x1=x+step*math.cos(angle)
    y1=y-step*math.sin(angle)
    return x1,y1

import math
def quadratic(a, b, c):
    if not isinstance (a,(int,float)) or not isinstance (b,(int,float)) or not isinstance (c,(int,float)):
        raise TypeError('bad operand type')
    if a==0:
        if b==0:
            if c==0:
                print('无穷解')
            else:
                print('无解')
        else:
            x1=-c/b
            return x1
    else:
        g=b**2-4*a*c
        if g>0:
            x1=(-b+math.sqrt(g))/(2*a)
            x2=(-b-math.sqrt(g))/(2*a)
            return x1,x2
        elif g==0:
            x1=(-b)/2*a
            return x1
        else:
            print('无解2')