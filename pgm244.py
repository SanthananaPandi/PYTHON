# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:57:13 2023
Construct a n list of integers and find the biggest element and index of the element using function
@author: santh
"""

a=[]
n=int(input("Enter the value of n :" ))
for i in range(n):
    d=int(input("Enter the value of d :"))
    a.append(d)
    
x=max(a)
y=a.index(x)
print(x)
print(y)