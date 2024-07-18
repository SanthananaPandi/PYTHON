# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 17:49:12 2024
Find the duplicate values in the list
@author: santh
"""

import random as rd
n=int(input("Enter the value of n : "))
a=[rd.randint(-100,100)for i in range(n)]
x=set(a)
d={}
for i in x:
    y=a.count(i)
    d[i]=y
print(d)
    
for j in d:
    if d[j]>1:
        b=d[j]
        print(j)
    else:
        pass
