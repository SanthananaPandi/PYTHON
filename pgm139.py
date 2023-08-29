# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:37:07 2023
Construct a n list of integers and find the sum of element of the list
@author: santh
"""
a=[]
i=0
n=int(input("Enter a value of n: "))
while i<=n-1:
    d=int(input("Enter the value of d: "))
    a.append(d)
    i=i+1
b=0
m=len(a)
j=0
while j<=m-1:
    b=b+a[j]
    j=j+1
print(b)
