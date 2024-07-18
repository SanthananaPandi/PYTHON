# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:59:32 2023
Interchange the biggest and smallest element of the list using function
@author: santh
"""

a=[]
n=int(input("Enter the value of n :" ))
for i in range(n):
    d=int(input("Enter the value of d :"))
    a.append(d)
    
x=max(a)
y=a.index(x)
e=min(a)
f=a.index(e)

a[y]=e
a[f]=x
print(a)