# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:08:34 2024
Call the functions by 15 times using different arguments
@author: santh
"""

def calculate(a):
    def product(b):
        s=a*b
        print(s)
    return product 

#main
n=int(input("Enter the value of n : "))
a=int(input("Enter the value of a : "))
m=calculate(a)
for i in range(n):
    m(i)