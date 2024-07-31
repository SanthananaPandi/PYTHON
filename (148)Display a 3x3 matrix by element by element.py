# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:34:10 2023
Construct a 3X3 matrix and display it by element by element(matrix format)
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
while k<=3:
    j=0
    while j<=2:
        print(a[k][j], end=" ")
        j=j+1
    print()
    k=k+1
