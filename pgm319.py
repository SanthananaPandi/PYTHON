# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 19:16:55 2024
Find out biggest number in the argument that we have passed
@author: santh
"""

def num(*x):
    z=0
    for i in x:
        if i>z:
            z=i
    return z
    
#main

a=num(1,2,3,4,5,6)
b=num(1.0,2.0,3.0,4.0)
c=num(1000,2000,3000,4000)
d=num(121,221,321,421)
print(a)
print(b)
print(c)
print(d)

