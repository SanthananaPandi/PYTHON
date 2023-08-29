# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 18:48:43 2023
Interchange the smallest and biggest element of the list
@author: santh
"""
a=[]
i=0
n=int(input("Enter the value of n: "))
while i<=n-1:
    d=int(input("Enter the value of d: "))
    a.append(d)
    i=i+1
b=0
f=0
m=len(a)
j=0
while j<=m-1:
    if a[j]>b:
        b=a[j]
        c=j
    elif a[j]<e:
        e=a[j]
        f=j
    else:
        pass
    j=j+1
a[c]=e
a[f]=b
print(a)