# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 18:58:22 2023
Smallest of three integer number using nested expression
@author: santh
"""
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=(a if a<c else c)if a<b else(b if b<c else c)
print(d,"is a smaller")

