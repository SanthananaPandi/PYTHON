# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:24:19 2024
Sum of two numbers using function within the function
@author: santh
"""

def calculate():
    def sum(a,b):
        s=a+b
        return s
    a=int(input("Enter the value of a : "))
    b=int(input("Enter the value of b : "))
    s=sum(a,b)
    print(s)
    
#main
calculate()