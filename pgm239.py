# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 11:11:45 2023
Sum of the element of the matrix
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
        m+=y
print(m)