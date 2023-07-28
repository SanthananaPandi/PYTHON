# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 18:47:58 2023
Biggest of three integer number using ternary expression
@author: santh
"""
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d= a if a>b else b
e= c if c>d else d
print(e,"is greater")

