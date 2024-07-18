# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 19:46:06 2023
Biggest element of the 3X3 matrix
@author: santh
"""
a=[]
b=0
while b < 3:
    c=[]
    n=3
    i=0
    while i < n:
        d=int(input("Enter the value of d: "))
        c.append(d)
        i=i + 1
    a.append(c)
    b=b+1

k=0
s=0
while k < 3:
    j = 0
    while j < 3:
        if a[k][j] > s:
            s=a[k][j]
        j=j+1
    k=k+1

print(s)

