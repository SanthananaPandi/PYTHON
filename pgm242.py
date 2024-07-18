# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:08:41 2023
Differences of two matrices
@author: santh
"""

a=[]
for i in range(3):
    b=[]
    for j in range(3):
        d=int(input("Enter the value of d : "))
        b.append(d)
    a.append(b)
    
c=[]
for i in range(3):
    e=[]
    for j in range(3):
        d=int(input("Enter the value of x : "))
        e.append(d)
    c.append(e)

f=[]
for i in range(3):
    g=[]
    for j in range(3):
        m=a[i][j] - c[i][j]
        g.append(m)
    f.append(g)
print(f)