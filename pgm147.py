# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 17:52:45 2023
Construct a 3X3 matrix and list a row by row
@author: santh
"""
a=[]
b=0
while b<=3:
    c=[]
    i=0
    n=3
    while i<=n-1:
        d=int(input("Enter the value of d: "))
        c.append(d)
        i=i+1
    a.append(c)
    b=b+1
k=0
while k<=3:
    print(a[k])
    k=k+1