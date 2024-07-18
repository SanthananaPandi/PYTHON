# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:09:55 2023
Sum of the element of the matrix
@author: santh
"""
a=[]
for i in range(3):
    c=[]
    for j in range(3):
        d=int(input("Enter the value of d: "))
        c.append(d)
    a.append(c)
    

m=0
for k in range(3):
    for y in range(3):
        m= a[k][y] + m
print(m)
