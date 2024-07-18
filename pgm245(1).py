# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 20:23:18 2023
Interchange the biggest and smallest element of the list using function and random package
@author: santh
"""

import random as rd
a=[]
n=int(input("Enter the value of n :" ))
for i in range(n):
    d=rd.randint(-100,100)
    a.append(d)
    
x=max(a)
y=a.index(x)
e=min(a)
f=a.index(e)

a[y]=e
a[f]=x
print(a)