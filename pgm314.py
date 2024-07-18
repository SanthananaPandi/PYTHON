# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:53:02 2024
Sum of two integers using keyword arguments
@author: santh
"""

def sum(a=10,b=20):
    s=a+b
    return s

#main
s=sum()
x=sum(b=100)
y=sum(b=200,a=100)
print(s)
print(x)
print(y)