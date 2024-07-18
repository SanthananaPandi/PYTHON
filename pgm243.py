# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:21:10 2023
Construct a n list of integers and find the biggest element of list using function(max)
@author: santh
"""

a=[]
n=int(input("Enter the value of n :" ))
for i in range(n):
    d=int(input("Enter the value of d :"))
    a.append(d)
    
x=max(a)
print(x)