# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:49:21 2023
Construct a n list of integers and find the biggest element of the list
@author: santh
"""
a=[]
n=int(input("Enter the value of n: "))
for i in range(n):
    d=int(input("Enter the value of d : "))
    a.append(d)

b=0
for i in a:
    if i > b:
        b=i
print(b)
