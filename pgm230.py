# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:55:47 2023
Interchange the biggest and smallest element of the list
@author: santh
"""

a=[]
n=int(input("Enter the value of n: "))
for i in range(n):
    d=int(input("Enter the value of d : "))
    a.append(d)

b=0
c=0
f=0
n=len(a)
for i in range(n):
    if a[i] > b:
        b=a[i]
        e=i
    elif a[i] < c:
        c=a[i]
        f=i
a[e]=c
a[f]=b
print(a)