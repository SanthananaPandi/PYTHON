# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:55:19 2024
Biggest of three numbers using keyword arguments
@author: santh
"""

def big(a=10,b=20,c=30):
    x=(a if a>c else c)if a>b else(b if b>c else c)
    return x

#main
x=big()
a=big(b=40)
b=big(b=60,a=70)
c=big(b=100,a=160,c=50)
print(x)
print(a)
print(b)
print(c)