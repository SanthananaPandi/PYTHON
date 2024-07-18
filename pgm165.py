# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:23:38 2023
Find the biggest and smallest of ten numbers using ternary expression
@author: santh
"""
a=0
b=0
for i in range(10):
    c=int(input("Enter the value of c: "))
    d=c if c>a else a
    e=c if c<b else b
print(d)
print(e)
