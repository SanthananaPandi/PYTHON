# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:19:02 2024
Find the biggest of three numbers by passing a function to the function
@author: santh
"""

def big(a,b,c):
    x=(a if a>c else c)if a>b else(b if b>c else c)
    return x

def calculate(a,b,c,x):
    y=x(a,b,c)
    print(y)
    
#main
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
calculate(a,b,c,big)