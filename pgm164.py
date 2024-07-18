# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:22:04 2023
Biggest of ten numbers
@author: santh
"""
b=0
for i in range(10):
    a=int(input("Enter the value of a: "))
    if a>b:
        b=a
print(b)
