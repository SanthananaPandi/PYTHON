# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:18:11 2024
Find the frequency count of the unique values
@author: santh
"""

import random as rd
n=int(input("Enter the value of n : "))
a=[rd.randint(-100,100)for i in range(n)]
x=set(a)
print(x)

for i in x:
    y=a.count(i)
    print(i,y)