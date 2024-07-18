# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:25:52 2024
Sum of two integer numbers using default arguments
@author: santh
"""

def sum(a=100,b=200):
    s=a+b
    return s

#main
s=sum()
x=sum(50)
y=sum(40,60)
print(s)
print(x)
print(y)