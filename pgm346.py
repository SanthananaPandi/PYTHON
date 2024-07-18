# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 17:48:36 2024
Sum of two numbers using lambda functions or anonymous function.
@author: santh
"""

sum=lambda x,y : x+y
x=int(input("Enter the value of x : "))
y=int(input("Enter the value of y : "))
z=sum(x,y)
print(z)