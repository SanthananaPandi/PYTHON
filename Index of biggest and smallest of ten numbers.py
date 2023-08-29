# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:42:50 2023
Index of biggest and smallest of ten numbers
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
e=0
m=len(a)
j=0
while j<=m-1:
    if a[j]>b:
        b=a[j]
        c=j
    elif a[j]<e:
        f=a[j]
        e=j
    else:
        pass
    j=j+1
print(c)
print(e)
