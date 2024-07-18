# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:07:13 2023
Display a 3X3 matrix by element by element
@author: santh
"""

a=[]
for i in range(3):
    c=[]
    for j in range(3):
        d=int(input("Enter the value of d: "))
        c.append(d)
    a.append(c)


for k in range(3):
    for y in range(3):
        print(a[k][y])