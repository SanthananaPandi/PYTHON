# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:31:53 2024
Biggest and smallest of three integer numbers using default arguments
@author: santh
"""

def big_small(a=100,b=500,c=400):
    x=(a if a>c else c)if a>b else(b if b>c else c)
    y=(a if a<c else c)if a<b else(b if b<c else c)
    return x,y

#main
x=big_small()
y=big_small(200)
z=big_small(400,700)
m=big_small(700,900,50)
print(x)
print(y)
print(z)
print(m)
