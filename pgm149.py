# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 19:29:51 2023
Construct 3X3 matrix and sum the each element of the matrix
@author: santh
"""
a=[]
b=0
while b<=3:
    c=[]
    n=3
    i=0
    while i<=n-1:
        d=int(input("Enter the value of d: "))
        c.append(d)
        i=i+1
    a.append(c)
    b=b+1
k=0
s=0
while k<=3:
    j=0
    while j<=2:
        s=s+a[k][j]
        j=j+1
    k=k+1
print(s)




