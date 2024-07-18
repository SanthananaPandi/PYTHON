# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:14:11 2023
Count the number of leap year between two limits
@author: santh
"""
c=0
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
for i in range(a,b):
    d=i%4
    if d==0:
        c=c+1
print(c)
