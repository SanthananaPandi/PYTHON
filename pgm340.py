# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 17:36:16 2024
Print the multiply and multiplier in a table format
@author: santh
"""

def calculate(a):
    def product(b):
        s=a*b
        return s
    return product 

#main
n=int(input("Enter the value of n : "))
a=int(input("Enter the value of a : "))
m=calculate(a)
for i in range(n):
    s= m(i)
    print(a,"*",i,"=", s)
    
    
    