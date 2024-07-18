# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 19:27:29 2024
Construct a set of n integer numbers using set comprehension
@author: santh
"""

n=int(input("Enter the value of n : "))
a={int(input("Enter the value of a : "))for i in range(n)}
print(a)