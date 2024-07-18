# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:04:47 2023
Construct a 3X3 matrix and list a row by row
@author: santh
"""
a=[]
for i in range(3):
    c=[]
    for j in range(3):
        d=int(input("Enter the value of d: "))
        c.append(d)
    a.append(c)
    
for i in range(3):
    print(a[i])
