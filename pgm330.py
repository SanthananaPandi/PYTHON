# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:22:36 2024
Biggest and smallest of three numbers by passing a function to the function
@author: santh
"""

def big_low(a,b,c):
    x=(a if a>c else c)if a>b else(b if b>c else c)
    y=(a if a<c else c)if a<b else(b if b<c else c)
    return x,y

def calculate(a,b,c,x):
    y=x(a,b,c)
    print(y)
    
#main
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
calculate(a,b,c,big_low)