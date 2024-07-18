# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 19:21:24 2024
Biggest and smallest number of arguments that we have passed
@author: santh
"""

def num(*x):
    z=0
    y=9999
    for i in x:
        if i>z:
            z=i
        if i<y:
            y=i
    return z,y

#main

a=num(1,2,3,4,5,6)
b=num(1.0,2.0,3.0,4.0)
c=num(1000,2000,3000,4000)
d=num(121,221,321,421)
print(a)
print(b)
print(c)
print(d)


