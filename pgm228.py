# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:50:52 2023
Find the index of the biggest element of the list
@author: santh
"""
a=[]
n=int(input("Enter the value of n: "))
for i in range(n):
    d=int(input("Enter the value of d : "))
    a.append(d)

n=len(a)
b=0
for i in range(n):
    if a[i] > b:
        b=a[i]
        c=i
print(c)
