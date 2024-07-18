# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 15:13:34 2023
Biggest element of the 3x3 matrix
@author: santh
"""

a=[]
for i in range(3):
    c=[]
    for j in range(3):
        d=int(input("Enter the value of d : "))
        c.append(d)
    a.append(c)
    
m=0
for k in a:
    for y in k:
        if y>m:
            m=y
print(m)