# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 22:53:43 2024
Product of two real numbers using function
@author: santh
"""

def product(x,y):
    s=x*y
    return s

#main
x=float(input("Enter the value of x : "))
y=float(input("Enter the value of y : "))
s=product(x,y)
print(s)
