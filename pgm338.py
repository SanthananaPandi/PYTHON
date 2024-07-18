# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:05:38 2024
Product of two integer numbers using closure function
@author: santh
"""

def calculate(a):
    def product(b):
        s=a*b
        print(s)
    return product
#main
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
m=calculate(a)
m(b)