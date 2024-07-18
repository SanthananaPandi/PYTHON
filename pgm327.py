# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:12:00 2024
Sum of two numbers using functions by passing a sum function
@author: santh
"""

def sum(a,b):
    s=a+b
    return s

def two(a,b,z):
    s=z(a,b)
    print(s)
    
#main
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
two(a,b,sum)