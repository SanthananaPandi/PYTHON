# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:59:46 2023
Interchange the  second smallest and  second biggest element of the list
@author: santh
"""

a=[]
n=int(input("Enter the value of n: "))
for i in range(n):
    d=int(input("Enter the value of d : "))
    a.append(d)

n=len(a)
b=0
for i in range(n):
    if a[i] > b:
        b=a[i]

c=0
n=len(a)
for i in range(n):
    if a[i]!=b:
        if a[i] > c:
            c=a[i]
            x=i
            
d=0
n=len(a)
for j in range(n):
    if a[j] <d:
        d=a[j]
        
y=0
e=0
n=len(a)
for j in range(n):
    if a[j] != d and a[j] < e:
        e=a[j]
        y=j
        
a[x]=e
a[y]=c
print(a)