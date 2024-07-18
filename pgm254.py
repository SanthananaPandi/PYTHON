# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 18:18:04 2023
Make all the leap years to zero using list comprehension(ternary expression).
@author: santh
"""

a=[0 if i % 4 ==0 else i for i in range(1000,3001)]
print(a)