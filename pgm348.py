# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 17:52:51 2024
Biggest of three numbers using lambda function
@author: santh
"""

Big=lambda a,b,c :(a if a>c else c)if a>b else(b if b>c else c)
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
x=Big(a,b,c)
print(x)