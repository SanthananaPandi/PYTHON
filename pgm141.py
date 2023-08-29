# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:41:21 2023
Find the element of the biggest element  of the list
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
    if a[j]>b:
        b=a[j]
        c=j
    else:
        pass
    j=j+1
print(c)
