# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:58:47 2024
Sum of two integers using closure functions
@author: santh
"""

def calculate():
    def inner(a,b):
        s=a+b
        print(s)
    return inner
#main
x=calculate()
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
x(a,b)
