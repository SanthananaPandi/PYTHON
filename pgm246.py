# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 20:02:24 2023
Construct a n list of integers and find the biggest element and index of the 
element using function and random package.
@author: santh
"""

import random as rd
a=[]
n=int(input("Enter the value of n : "))
for i in range(n):
    d=rd.randint(-100,100)
    print(d)
    a.append(d)
    
x=max(a)
y=a.index(x)
print(x)
print(y)
