# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:57:21 2023
Find out the second biggest number
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

c=0
n=len(a)
for i in range(n):
    if a[i]!=b:"""use and oprerator"""
        if a[i] > c:
            c=a[i]

print(c)