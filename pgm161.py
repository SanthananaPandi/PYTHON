# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:16:04 2023
Count the number of odd number and even number between two limits
@author: santh
"""
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=0
d=0
for i in range(a,b):
    e=i%2
    if e==0:
        c=c+1
    else:
        d=d+1
print(c)
print(d)