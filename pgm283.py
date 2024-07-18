# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:56:55 2024
Construct a set of n ordinary numbers and print it
@author: santh
"""

a=set()
n=int(input("Enter the value of n : "))
for i in range(n):
    b=int(input("Enter the value of b : "))
    a.add(b)
print(a)