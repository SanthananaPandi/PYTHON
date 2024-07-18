# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 20:25:29 2023
Construct a n list of integers and find the biggest element of list using function and random package(max)
@author: santh
"""

import random as rd
a=[]
n=int(input("Enter the value of n :" ))
for i in range(n):
    d=rd.randint(-100,100)
    a.append(d)
    
x=max(a)
print(x)