# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:28:17 2024
Biggest of three integer numbers using default arguments
@author: santh
"""

def big(a=100,b=500,c=300):
    x=(a if a>c else c)if a>b else(b if b>c else c)
    return x

#main
x=big()
y=big(560)
z=big(800,600)
m=big(900,100,200)
print(x)
print(y)
print(z)
print(m)