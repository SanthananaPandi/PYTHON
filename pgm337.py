# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:59:52 2024
Sum of two integers using closure function
@author: santh
"""

def calculate(a):
    def sum(b):
        s=a+b
        print(s)
    return sum 
#main
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
m=calculate(a)
m(b)