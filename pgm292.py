# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 17:45:13 2024
Store a frequency count in the dictionary
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
